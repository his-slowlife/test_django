import datetime
from django.db import models

from django.utils import timezone

from django import forms



class DateInput(forms.DateInput):
    input_type = 'date'

class MyModelForm(forms.ModelForm):
    class Meta:

        fields = '__all__'
        widgets = {
            'my_date': DateInput(attrs={'type': 'date'})
        }
        

class Booking(models.Model):
    booking_title = models.CharField('Номер бронирования', max_length = 200)
    booking_text = models.TextField('Описание бронирования')
    pub_date = models.DateTimeField('Дата бронирования')

    def __str__(self):
        return self.booking_title

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days = 3))

    class Meta:
        verbose_name = 'Кабинет'
        verbose_name_plural = 'Кабинеты'
        
class Comment(models.Model):
    booking = models.ForeignKey(Booking, on_delete = models.CASCADE)
    author_name = models.CharField('Имя', max_length = 50)
    comment_text = models.CharField('Описание бронирования', max_length = 200)
    booking_date_input = models.CharField('Дата', max_length = 50)
    booking_time_input = models.CharField('Время', max_length = 50)
    booking_hours = models.CharField('Длительность', max_length = 5)

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'
