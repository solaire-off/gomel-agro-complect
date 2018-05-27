from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.template.defaultfilters import slugify
from transliterate import translit

def TranslitToEn(text):
    return translit(text, 'ru', reversed=True).lower()

def isBlank(myString):
    return not (myString and myString.strip())

class Tag(models.Model):
    title = models.CharField(verbose_name="Наименование", max_length=200)
    ceo_description = models.TextField(verbose_name="Описание", blank=True, null=True)
    url = models.CharField(verbose_name="Ссылка",max_length=200, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now, editable=False, verbose_name="Дата добавления")

    class Meta:
        verbose_name = 'Метку'
        verbose_name_plural = 'Метки'
        ordering = ['-created_date']


    def get_absolute_url(self):
        return reverse('news_by_tag', args=[self.url])

    def save(self, *args, **kwargs):
        if isBlank(self.url):
            self.url = slugify(TranslitToEn(self.title))
        super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField(verbose_name="Новости", max_length=200)
    content = models.TextField(verbose_name="Контент")
    tags = models.ManyToManyField(Tag, blank=True, verbose_name="Метки")
    published = models.BooleanField(default=1,verbose_name="Опубликована")
    created_date = models.DateTimeField(default=timezone.now, verbose_name="Дата добавления")

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_date']

    def __str__(self):
        return self.title
