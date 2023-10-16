from django.contrib import admin

from services.document_module.models import Document, DocumentSearchHistory


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'email', 'created_at')
    search_fields = ('title', 'owner__email', 'description')

    def email(self, obj):
        return obj.owner.email


@admin.register(DocumentSearchHistory)
class DocumentHistoryAdmin(admin.ModelAdmin):
    list_display = ('search_query', )
    search_fields = ('search_query', )
