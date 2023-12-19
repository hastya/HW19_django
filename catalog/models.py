from django.db import models


NULLABLE = {'blank': True, 'null': True}
# Create your models here.

class Feedback(models.Model):
    name = models.CharField(max_length=50, verbose_name='имя')
    email = models.EmailField(verbose_name='Email')
    message = models.TextField(verbose_name='Сообщение', **NULLABLE)

    is_active = models.BooleanField(default=True, verbose_name='получено')

    def __str__(self):
        return f'{self.name} - {self.email}'

    class Meta:
        verbose_name = 'сообщение'
        verbose_name = 'сообщения'
        ordering = ('name',)
