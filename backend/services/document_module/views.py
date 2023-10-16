from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q, Max
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from .forms import CreateDocumentForm
from .mixins import UserDocumentMixin
from .utils import save_history_search_document


class DocumentListView(LoginRequiredMixin, UserDocumentMixin, ListView):
    template_name = 'document/documents.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query_param'] = self.request.GET.get('search')
        context['page_query_param'] = self.request.GET.get('page')
        return context

    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = self.queryset.filter(owner=self.request.user)
        if query is not None:
            object_list = object_list.filter(owner=self.request.user).filter(
                Q(title__icontains=query) | Q(description__icontains=query)
            )
            save_history_search_document(queryset=object_list, search_query=query)
        return object_list


class DocumentDetailView(LoginRequiredMixin, UserDocumentMixin, DetailView):
    pk_url_kwarg = 'pk'
    template_name = 'document/get_document.html'

    def get_queryset(self):
        object_list = self.queryset.prefetch_related('history_search_documents').annotate(
            time_last_search=Max('history_search_documents__created_at'))
        return object_list


class DocumentDeleteView(LoginRequiredMixin, UserDocumentMixin, DeleteView):
    success_url = reverse_lazy('document:documents')
    template_name = 'document/delete_document.html'


class DocumentUpdateView(LoginRequiredMixin, UserDocumentMixin, UpdateView):
    fields = [
        'title',
        'description',
        'status'
    ]
    template_name = 'document/add_document.html'
    success_url = reverse_lazy('document:documents')


class DocumentCreateView(LoginRequiredMixin, UserDocumentMixin, CreateView):
    template_name = 'document/add_document.html'
    form_class = CreateDocumentForm
    success_url = reverse_lazy('document:documents')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.owner = self.request.user
        obj.save()
        return redirect(self.success_url)
