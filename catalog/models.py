from django.db import models
from django.utils import timezone
from transliterate import translit

def TranslitToEn(text):
    return translit(text, 'ru', reversed=True)

def UploadImageForItem(object,filename):
    if object.url:
        return 'items/%s/%s'%(object.url, filename)
    return 'items/%s/%s'%(TranslitToEn(object.title),filename)


class Item(models.Model):
    title = models.CharField(max_length=200, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")
    catagory = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL, verbose_name="Категория")
    image = models.FileField(upload_to=UploadImageForItem, blank=True, null=True,verbose_name="Изображение")
    url = models.CharField(max_length=200, null=True, blank=True, verbose_name="Ссылка")
    publish = models.BooleanField(default=1,verbose_name="Опубликовано")
    created_date = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def publish(self):
        self.publish = True
        self.save()

    def hide(self):
        self.publish = False
        self.save()

    def __str__(self):
        return self.title



class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name="Наименование")
    description  = models.TextField(verbose_name="Описание")
    created_date = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title
