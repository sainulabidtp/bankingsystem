from django.db import models
from django.shortcuts import redirect
from django.utils.text import slugify  # Import slugify function



# Create your models here.
class District(models.Model):
    name = models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    wikipedia = models.CharField(max_length=250)


    class Meta:
        ordering = ('name',)
        verbose_name = 'district'
        verbose_name_plural = 'districts'

    def get_url(self):
        return self.wikipedia
    def __str__(self):
        return '{}'.format(self.name)
class Branch(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.name)

class ApplicationForm(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])
    phone_number = models.CharField(max_length=15)
    mail_id = models.EmailField()
    address = models.TextField()

    district = models.ForeignKey('District', on_delete=models.CASCADE)
    branch = models.ForeignKey('Branch', on_delete=models.CASCADE)
    account_type = models.CharField(max_length=20, choices=[('savings', 'Savings Account'), ('current', 'Current Account')])
    materials_provided = models.ManyToManyField('MaterialProvided')

    def __str__(self):
        return '{}'.format(self.name)

class MaterialProvided(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.name)
