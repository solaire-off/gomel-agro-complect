from django import forms
from ckeditor.widgets import CKEditorWidget
from django.utils.safestring import mark_safe
from .models import Item, Category, Detail

class AdminImageWidget(forms.FileInput):
    """
    A ImageField Widget for admin that shows a thumbnail.
    Taken from https://djangosnippets.org/snippets/1580/
    """

    def __init__(self, attrs={}):
        super(AdminImageWidget, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        output = []
        if value and hasattr(value, "url"):
            output.append(('<a target="_blank" href="%s">'
                           '<img src="%s" style="height: 250px;" /></a> <br /><br />'
                           % (value.url, value.url)))
        output.append(super(AdminImageWidget, self).render(name, value, attrs))
        return mark_safe(''.join(output))


class ItemAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget(), label="Описание")
    image =  forms.ImageField(label='Изображение', widget=AdminImageWidget)

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
    image =  forms.ImageField(label='Изображение', widget=AdminImageWidget)

    class Meta:
        model = Detail
        fields = '__all__'
