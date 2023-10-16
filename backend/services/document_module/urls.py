from django.urls import path
from . import views

app_name = 'document'

urlpatterns = [
    path('documents/', views.DocumentListView.as_view(), name='documents'),
    path('document/<slug:pk>/', views.DocumentDetailView.as_view(), name='get_document'),
    path('document/<slug:pk>/update/', views.DocumentUpdateView.as_view(), name='update_document'),
    path('document/<slug:pk>/delete/', views.DocumentDeleteView.as_view(), name='delete_document'),
    path('document/create/', views.DocumentCreateView.as_view(), name='document_create'),
]
