from django.db import models
from django.urls import reverse


class Group(models.Model):
    title = models.CharField(max_length=128, verbose_name="Название")
    slug = models.SlugField(max_length=128, unique=True, verbose_name='URL')
    course = models.SmallIntegerField(verbose_name="Курс", blank=True, default=0)
    content = models.TextField(verbose_name="Расписание", blank=True, default='NullSchedule')

    def get_absolute_url(self):
        return reverse('schedule', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
        verbose_name = "Группа"
        verbose_name_plural = "Группы"


class WeekSchedule(models.Model):
    title = models.CharField(max_length=128, verbose_name='Название')
    slug = models.SlugField(max_length=128, unique=True, verbose_name='URL')
    group = models.ForeignKey(Group, on_delete=models.PROTECT, related_name='schedule')
    content = models.TextField(verbose_name='Расписание')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('schedule', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = "Расписание"
        verbose_name_plural = "Расписания"







