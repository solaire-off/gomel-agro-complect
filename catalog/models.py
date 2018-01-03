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
    title = models.CharField(max_length=200)
    description = models.TextField()
    catagory = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)
    image = models.FileField(upload_to=UploadImageForItem, blank=True, null=True)
    url = models.CharField(max_length=200)
    publish = models.BooleanField(default=0)
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.publish = True
        self.save()

    def hide(self):
        self.publish = False
        self.save()

    def __str__(self):
        return self.title



class Category(models.Model):
    title = models.CharField(max_length=200)
    description  = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
