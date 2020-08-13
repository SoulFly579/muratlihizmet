from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django import forms
from django.forms import ModelForm, TextInput, Textarea

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(blank = True , upload_to='images/')
    slug = models.SlugField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Haberler(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    content = RichTextUploadingField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-create_at']

    def __str__(self):
        return self.title

class Setting(models.Model):
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    company = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)
    fax = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    icon = models.ImageField(blank=True, upload_to='images/')
    facebook = models.CharField(max_length=50)
    instagram = models.CharField(max_length=50)
    twitter = models.CharField(max_length=50)
    aboutus = RichTextUploadingField()
    contact = RichTextUploadingField()
    kunye = RichTextUploadingField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
class Image(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    yazar = models.ImageField(upload_to='images/')