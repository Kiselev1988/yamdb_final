from datetime import datetime

from django.core.validators import MaxValueValidator
from django.db import models


def get_current_year():
    """Возвращает текущий год."""
    return datetime.now().year


class CategoryGenre(models.Model):
    """Общая часть для моделей Category и Genre."""
    name = models.CharField(
        'Название',
        max_length=256,
    )
    slug = models.SlugField(
        'Короткое название',
        max_length=50,
        unique=True
    )

    class Meta:
        ordering = ('name',)


class Category(CategoryGenre):
    """Модель Category."""
    class Meta():
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'Категория - {self.name}'


class Genre(CategoryGenre):
    """Модель Genre."""
    class Meta():
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return f'Жанр - {self.name}'


class Title(models.Model):
    """Модель произведения."""
    name = models.TextField(
        verbose_name='Название произведения',
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name='Описание',
    )
    genre = models.ManyToManyField(
        Genre,
        blank=True,
        related_name='titles',
        verbose_name='Жанр',
    )
    year = models.PositiveSmallIntegerField(
        validators=(
            MaxValueValidator(
                get_current_year,
                message='Нельзя указывать год, больше текущего',
            ),

        ),
        verbose_name='Год',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='titles',
        verbose_name='Категория',
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return (
            f'Произведение {self.name} - Категория {self.category}'
            f'Жанр {self.genre} - Год релиза {self.year}'
        )
