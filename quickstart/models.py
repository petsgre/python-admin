from django.db import models

# Create your models here.


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=240, default='')
    phone = models.CharField(
        max_length=50, blank=False, default='13111111111')
    password = models.CharField(
        max_length=50, blank=False, default='123')
    created = models.DateTimeField(auto_now_add=True)
