from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from services.document_module.constants import DOCUMENT_STATUS


class Document(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    description = models.TextField(max_length=2000, verbose_name='Description',
                                   null=True,
                                   blank=True)
    status = models.CharField(choices=DOCUMENT_STATUS,
                              max_length=30,
                              verbose_name='Status')
    owner = models.ForeignKey(User,
                              verbose_name='Owner',
                              on_delete=models.deletion.CASCADE,
                              related_name='owner')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

    def get_absolute_url(self):
        return reverse('document:get_document', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.title}'


class DocumentSearchHistory(models.Model):
    search_query = models.CharField(max_length=255, verbose_name='Search Query')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    document = models.ManyToManyField(Document,
                                      verbose_name='Document',
                                      related_name='history_search_documents')

    def __str__(self):
        return f'{self.search_query}'
