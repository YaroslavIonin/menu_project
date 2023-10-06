from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from .menu import Menu


class MenuItem(MPTTModel):
    title = models.CharField(
        unique=True,
        max_length=50,
        verbose_name='Название',
    )
    slug = models.SlugField(
        verbose_name='Cлаг для url',
    )
    menu = models.OneToOneField(
        Menu,
        on_delete=models.CASCADE,
        verbose_name='Меню',
        help_text='Только для пунктов без родительских элементов',
        blank=True,
        null=True,
    )
    parent = TreeForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='children',
        on_delete=models.CASCADE,
        verbose_name='Пункт уровня выше',
    )

    class MPTTMeta:
        order_insertion_by = ('title',)

    class Meta:
        verbose_name = "Элемент меню"
        verbose_name_plural = "Элементы меню"

    def __str__(self):
        return self.title

    @property
    def get_absolute_url(self):
        url, slug = '', self.slug
        parent = self.parent

        while parent:
            slug = parent.slug + '/' + slug
            parent = parent.parent

        return slug
