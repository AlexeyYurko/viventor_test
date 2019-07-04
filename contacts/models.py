from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse


class Contact(models.Model):
    first_name = models.CharField(
        verbose_name='first name', max_length=30, blank=True, default='')
    last_name = models.CharField(
        verbose_name='last name', max_length=30, blank=True, default='')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. "
                                         "Up to 15 digits allowed.")
    phone_number = models.CharField(verbose_name='phone number', validators=[phone_regex], max_length=17, blank=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    birth_date = models.DateField()

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse('contact-detail', args=[str(self.id)])
