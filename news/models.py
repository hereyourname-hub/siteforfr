from django.db import models


class Articles(models.Model):
    title = models.CharField('Название: ', max_length=250)
    anons = models.CharField('Цитата: ', max_length=250)
    full_text = models.TextField('Стих: ')
    date = models.DateTimeField('Дата публикации: ')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Стих'
        verbose_name_plural = 'Стихи'

