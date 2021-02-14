from django.db import models
from datetime import datetime


class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')
    reminder = models.DateTimeField
    date = models.DateTimeField('Дата создания', default=datetime.now())

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
