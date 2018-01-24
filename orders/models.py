from django.db import models
from django.utils import timezone
from catalog.models import Item

class Order(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    phone = models.CharField(max_length=100, verbose_name="Телефон")
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, verbose_name="Товар", null=True)
    note = models.CharField(max_length=300, verbose_name="Примечание", blank=True, null=True)
    processed = models.BooleanField(default=0, verbose_name="Принята")
    created_date = models.DateTimeField(default=timezone.now, verbose_name="Дата отправки")

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return self.name + ' - ' + self.phone


