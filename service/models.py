from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.template.defaultfilters import slugify
from transliterate import translit

def UploadImageForService(object,filename):
    return 'service/%s/%s'%(object.url, filename)

def UploadImageForServiceCategory(object,filename):
    return 'service_category/%s/%s'%(object.url, filename)

def TranslitToEn(text):
    return translit(text, 'ru', reversed=True).lower()

def isBlank(myString):
    return not (myString and myString.strip())

class Category(models.Model):
    title = models.CharField(verbose_name="Наименование", max_length=200)
    image = models.FileField(upload_to=UploadImageForServiceCategory, blank=True, null=True, verbose_name="Изображение")
    ceo_description = models.TextField(verbose_name="Короткое описание", blank=True, null=True)
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    url = models.CharField(verbose_name="Ссылка",max_length=200, blank=True, null=True)
    published = models.BooleanField(default=1,verbose_name="Опубликована")
    created_date = models.DateTimeField(default=timezone.now, editable=False, verbose_name="Дата добавления")

    class Meta:
        verbose_name = 'Тип услуги'
        verbose_name_plural = 'Типы услуг'
        ordering = ['-created_date']


    def get_absolute_url(self):
        return reverse('service_by_category', args=[self.url])

    def save(self, *args, **kwargs):
        if isBlank(self.url):
            self.url = slugify(TranslitToEn(self.title))
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class CategoryImage(models.Model):
    category = models.ForeignKey('Category', related_name = 'images')
    image = models.ImageField()

    def __str__(self):
        return str(self.id)

class Service(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=200)
    image = models.FileField(upload_to=UploadImageForService, blank=True, null=True, verbose_name="Изображение")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    content = models.TextField(verbose_name="Контент")
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL, verbose_name="Категория")
    url = models.CharField(max_length=200, verbose_name="Ссылка", blank=True, null=True)
    published = models.BooleanField(default=1,verbose_name="Опубликована")
    created_date = models.DateTimeField(default=timezone.now, verbose_name="Дата добавления")

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ['-created_date']

    def save(self, *args, **kwargs):
        if isBlank(self.url):
            self.url = slugify(TranslitToEn(self.title))
        super(Service, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('service_detail',
                        args=[self.category.url,
                              self.url])

    def __str__(self):
        return self.title
