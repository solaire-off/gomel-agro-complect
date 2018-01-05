from django import forms
from ckeditor.widgets import CKEditorWidget

from .models import Item, Category, Detail

class ItemAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget(), label="Описание")

    class Meta:
        model = Item
        fields = '__all__'


class CategoryAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget(), label="Описание")

    class Meta:
        model = Category
        fields = '__all__'

class DetailAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget(), label="Описание")

    class Meta:
        model = Detail
        fields = '__all__'
