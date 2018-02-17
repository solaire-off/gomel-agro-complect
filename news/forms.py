from django import forms
from ckeditor.widgets import CKEditorWidget
from django.utils.safestring import mark_safe
from .models import News


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(required=False, widget=CKEditorWidget(), label="Описание")

    class Meta:
        model = News
        fields = '__all__'
