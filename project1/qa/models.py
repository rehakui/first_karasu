from django.db import models
from django.utils import timezone



class Category(models.Model):
    name = models.CharField('カテゴリ名', max_length=200)

    def __str__(self):
        return self.name


class Day(models.Model):
    title = models.CharField('タイトル', max_length=200)
    text = models.TextField('本文')
    date = models.DateTimeField('日付', default=timezone.now)
    category = models.ForeignKey(Category, verbose_name='カテゴリ', on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField('名前', max_length=30, default='')
    text = models.TextField('本文')
    day = models.ForeignKey(Day, verbose_name='紐づく記事', on_delete=models.PROTECT)
    date = models.DateTimeField('日付', default=timezone.now)

    def __str__(self):
        return self.text[:10]
