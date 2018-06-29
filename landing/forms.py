from django import forms
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe
from .models import TextBlock, ImageItem

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
                '<img src="%s" style="height: 250px; max-width: 500px; object-fit: contain;" /></a> <br /><br />'
                           % (value.url, value.url)))
        output.append(super(AdminImageWidget, self).render(name, value, attrs))
        return mark_safe(''.join(output))


class ImageItemAdminForm(forms.ModelForm):
    source = forms.ImageField(label='Изображение', widget=AdminImageWidget)

    class Meta:
        model = ImageItem
        fields = '__all__'


class TextBlockAdminForm(forms.ModelForm):
    extend_content = forms.CharField(required=False, widget=CKEditorUploadingWidget(), label="Расширенный редактор контента")

    class Meta:
        model = TextBlock
        fields = '__all__'

