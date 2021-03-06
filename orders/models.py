from django.db import models
from django.utils import timezone
from catalog.models import Item

class Order(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    phone = models.CharField(max_length=100, verbose_name="Телефон")
    category  = models.CharField(max_length=300, verbose_name="Категория", blank=True, null=True)
    topic = models.CharField(max_length=300, verbose_name="Тема", blank=True, null=True)
    note = models.TextField(max_length=300, verbose_name="Примечание", blank=True, null=True)
    processed = models.BooleanField(default=0, verbose_name="Принята")
    created_date = models.DateTimeField(default=timezone.now, verbose_name="Дата и время отправки")
    created_date_format = models.DateField(default=timezone.now, verbose_name="Дата отправки")


    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-created_date']

    def __str__(self):
        return self.name + ' - ' + self.phone


