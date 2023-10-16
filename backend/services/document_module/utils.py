from services.document_module.models import DocumentSearchHistory, Document


def save_history_search_document(queryset: Document, search_query: str):
    history = DocumentSearchHistory.objects.create(search_query=search_query)
    history.document.add(*queryset)
    history.save()
