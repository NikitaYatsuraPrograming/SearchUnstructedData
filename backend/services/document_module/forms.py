from django import forms
from services.document_module.constants import DOCUMENT_STATUS
from services.document_module.models import Document


class CreateDocumentForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter Title', 'class': 'form-control'}
        ))

    description = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-control'}
        ))

    status = forms.ChoiceField(
        choices=DOCUMENT_STATUS,
        widget=forms.Select(
            attrs={'class': 'form-control'}
        ))

    class Meta:
        model = Document
        fields = ['title', 'description', 'status']
