from services.document_module.models import Document
from settings import LOGIN_URL


class UserDocumentMixin:
    login_url = LOGIN_URL
    model = Document
    queryset = Document.objects.all()

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
