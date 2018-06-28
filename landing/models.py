from django.db import models
from django.utils import timezone

def UploadImageForGallery(object,filename):
    return 'gallery/%s/%s'%(object.pk, filename)

class ImageItem(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    custom_style = models.CharField(max_length=300, verbose_name='Стили', blank=True, null=True, help_text='В этом поле вы можете задать css для изображения, если это предусмотрено данной группой изображений')
    description = models.TextField(verbose_name='Описание', blank=True,null=True)
    href = models.CharField(max_length=500,verbose_name='Ссылка', blank=True,null=True, help_text='Если это предусмотрено шаблоном, при клике на картинку произойдет переход по заданной ссылке')
    source = models.FileField(upload_to=UploadImageForGallery, verbose_name="Изображение")
    identifier = models.CharField(max_length=100, verbose_name='Идентификатор группы', blank=True,null=True)
    created_date = models.DateTimeField(default=timezone.now, editable=False, verbose_name="Дата добавления")

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        ordering = ['-created_date']

    def get_source_url(self):
        if self.source:
            return self.source.url
        return '-'

    def __str__(self):
        return self.title

class TextBlock(models.Model):
    title = models.CharField(max_length=100, verbose_name='Имя блока')
    identifier = models.CharField(max_length=100, verbose_name='Идентификатор блока')
    content = models.TextField(verbose_name='Контент блока', help_text='Если в блоке нужен простой текст, используйте это поле', blank=True, null=True)
    extend_content = models.TextField(verbose_name='Расширенный редактор блока', blank=True, null=True)
    is_extend = models.BooleanField(default=False, verbose_name='Выводить контент из расширенного редактора')
    created_date = models.DateTimeField(default=timezone.now, editable=False, verbose_name="Дата добавления")

    class Meta:
        verbose_name = 'Блок текста'
        verbose_name_plural = 'Блоки текста'
        ordering = ['-created_date']

    def __str__(self):
        return self.title







