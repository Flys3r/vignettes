from django.contrib.auth.models import Group, Permission
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    magic_number = models.IntegerField()
    role = models.CharField(max_length=50)

    
    groups = models.ManyToManyField(Group, verbose_name='groups', blank=True, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, verbose_name='user permissions', blank=True, related_name='custom_user_permissions')

class Category(models.Model):
    name = models.CharField(max_length=100)
    enabled = models.BooleanField(default=True)

class CardSize(models.Model):
    name = models.CharField(max_length=100)
    width = models.IntegerField()
    height = models.IntegerField()

class Card(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    music = models.FileField(upload_to='music/', null=True, blank=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    size = models.ForeignKey(CardSize, on_delete=models.CASCADE)
    deleted = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateField(auto_now_add=True)
