from django.db import models

BLANK_NULL_TRUE = {"blank": True, "null": True}


class BlogPost(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.CharField(max_length=150, **BLANK_NULL_TRUE)
    content = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(**BLANK_NULL_TRUE, verbose_name="Превью")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    views_count = models.IntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
        ordering = ['created_at']
