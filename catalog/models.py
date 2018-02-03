from django.db import models
from django.utils import timezone
from transliterate import translit
from django.template.defaultfilters import slugify

def TranslitToEn(text):
    return translit(text, 'ru', reversed=True).lower()

def UploadImageForItem(object,filename):
    return 'items/%s/%s'%(object.url, filename)

def UploadImageForDetail(object,filename):
    return 'items/%s/%s'%(object.url, filename)

def isBlank(myString):
    return not (myString and myString.strip())


class Item(models.Model):
    title = models.CharField(max_length=200, verbose_name="Наименование", help_text="Название или модель оборудования")
    description = models.TextField(verbose_name="Описание")
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL, verbose_name="Категория", help_text="Укажите категорию оборудования для удобной фильтрации")
    image = models.FileField(upload_to=UploadImageForItem, blank=True, null=True, verbose_name="Изображение")
    url = models.CharField(max_length=200, null=True, blank=True, verbose_name="Ссылка", help_text="Если оставить поле пустым, ссылка сгенерируется автоматическ из наименования")
    published = models.BooleanField(default=1,verbose_name="Опубликовано", help_text="Если оборудование не опубликовано, оно не будет отображаться в каталоге")
    created_date = models.DateTimeField(default=timezone.now, editable=False, verbose_name="Дата добавления")

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def save(self, *args, **kwargs):
        if isBlank(self.url):
            self.url = slugify(TranslitToEn(self.title))
        super(Item, self).save(*args, **kwargs)

    def __str__(self):
        return self.title



class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name="Наименование")
    url = models.CharField(max_length=200, verbose_name="Ссылка", blank=True, null=True, help_text="По ссылке будет доступно оборудование из данной категории. Если оставить поле пустым, ссылка автоматически сгенерируется из наименования.")
    description  = models.TextField(verbose_name="Описание", blank=True, null=True)
    published = models.BooleanField(default=1, verbose_name="Опубликовано", help_text="Если категория не опубликована, она и всё обородование, принадлжащее этой категории, не будут доступны в каталоге")
    created_date = models.DateTimeField(default=timezone.now, editable=False, verbose_name="Дата добавления")

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def save(self, *args, **kwargs):
        if isBlank(self.url):
            self.url = slugify(TranslitToEn(self.title))
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Detail(models.Model):
    title = models.CharField(max_length=200, verbose_name="Наименование", help_text="Название или маркировка запчасти")
    items = models.ManyToManyField("Item",verbose_name="Изделия", help_text="Укажите для какого оборудование подойдет данная деталь.")
    image = models.FileField(upload_to=UploadImageForDetail, blank=True, null=True,verbose_name="Изображение")
    published = models.BooleanField(default=1,verbose_name="Опубликовано", help_text="Если деталь не опубликована, она не будет отображаться в каталоге")
    created_date = models.DateTimeField(default=timezone.now, editable=False, verbose_name="Дата добавления")

    class Meta:
        verbose_name = "Запчасть"
        verbose_name_plural = "Запчасти"

    def __str__(self):
        return self.title
