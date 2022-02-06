from django.db import models
from django.urls import reverse

class Article(models.Model):
    name = models.CharField(max_length=200)
    number = models.CharField(max_length=20)
    date = models.DateField(max_length=20)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('article-detail', args=[str(self.id)])

class Client(models.Model):
    client_name = models.CharField(max_length=200)
    client_date = models.DateField(max_length=100)
    client_city = models.CharField(max_length=20)

    def __str__(self):
        return self.client_name

    def get_absolute_url(self):
        return reverse('client-detail', args=[str(self.id)])

class Contacts(models.Model):
    contact_name = models.CharField(max_length=100)
    contact_address = models.CharField(max_length=200)
    contact_mobile = models.CharField(max_length=12)
    contact_email = models.EmailField(max_length=20)

    def __str__(self):
        return self.contact_name

    def get_absolute_url(self):
        return reverse('contact-detail', args=[str(self.id)])

