# -*- coding: utf-8 -*-
from datetime import date, datetime
from django.utils import timezone
from django.db import models
from coaches.models import Coach
# Create your models here.


class Course (models.Model):
    name = models.CharField(verbose_name=u'Название', max_length=20)
    info = models.CharField(verbose_name=u'Короткое описание',null=True, blank=True, max_length=200)
    discription = models.TextField(verbose_name=u'Про курс', null=True, blank=True)
    logo = models.ImageField(upload_to='static/images/Courses/', verbose_name=u'Лого',null=True, blank=True)
    slider = models.ImageField(upload_to='static/images/Courses/', verbose_name=u'Слайдер',null=True, blank=True)
    teacher = models.ForeignKey(Coach, blank=True, null=True, related_name='coach_courses', verbose_name=u'Преподаватель')
    assistent = models.ForeignKey(Coach, blank=True, null=True, related_name='assistant_courses', verbose_name=u'Ассистент')
    start = models.DateField(blank=True, null=True, verbose_name=u'Начало курса')
    finish = models.DateField(blank=True, null=True, verbose_name=u'Окончание курса')
    price = models.IntegerField(default=0, verbose_name=u'Стоимость курса')

    def __unicode__(self):
        return self.name


class Lesson (models.Model):
    theme = models.CharField(verbose_name=u'Тема урока', max_length=40)
    discription = models.TextField(verbose_name=u'Описание урока', null=True, blank=True)
    course = models.ForeignKey(Course)
    number = models.PositiveIntegerField(verbose_name=u'Номер урока')

    def __unicode__(self):
        return str(self.number) + ' ' + self.theme


class Comment (models.Model):
    autor = models.CharField(verbose_name=u'Автор', max_length=30, default=u'Гость')
    discription = models.TextField(verbose_name=u'Отзыв')
    course = models.ForeignKey(Course)
    date_public = models.DateTimeField(verbose_name=u'Время создания', editable=True, auto_now_add=True, auto_now=True)

    def __unicode__(self):
        return self.autor
