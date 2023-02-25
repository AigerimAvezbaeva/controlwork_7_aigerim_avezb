from django.db import models


# Create your models here.
class GuestBook(models.Model):
    STATUS_CHOICES = (
        ('active', 'Активная'),
        ('blocked', 'Заблокирована')
    )
    fullname = models.CharField(max_length=300, blank=False, null=False, verbose_name='Имя гостя')
    email = models.EmailField()
    text = models.TextField(max_length=3000, null=False, verbose_name='Текст записи')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, blank=False,  default='active', verbose_name='Статус записи')
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата и время создания")
    updated_at = models.DateField(auto_now=True, verbose_name="Дата и время обновления")

    class Meta:
        verbose_name = 'Гостевая книга'
