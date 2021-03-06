from django import forms
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe
from .models import Service, Category


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

class ServiceAdminForm(forms.ModelForm):
    content = forms.CharField(required=False, widget=CKEditorUploadingWidget(), label="Контент")
    image =  forms.ImageField(label='Изображение', widget=AdminImageWidget)

    class Meta:
        model = Service
        fields = '__all__'

class CategoryAdminForm(forms.ModelForm):
    description = forms.CharField(required=False, widget=CKEditorUploadingWidget(), label="Контент")
    image =  forms.ImageField(label='Изображение', widget=AdminImageWidget)

    class Meta:
        model = Category
        fields = '__all__'
