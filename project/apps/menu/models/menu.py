from django.db import models


class Menu(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Название меню'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'
