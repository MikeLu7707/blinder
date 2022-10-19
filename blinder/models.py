import email
from telnetlib import STATUS
from tkinter import CASCADE
from turtle import update
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Book(models.Model): #models is a file generated for us by django and Model is a class begin inherited
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.title
        
class Post(models.Model):
    STATUS_CHOICES =(
        ('draft', 'Draft'),
        ('published', 'Published'),
    ) 
    title =  models.CharField(max_length=255)
    post_image = models.ImageField(blank=True, null=True)
    slug = models.CharField(max_length=255, unique_for_date = 'publish')
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name= 'blog_post')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    create = models.DateField(auto_now_add= True)
    update = models.DateField(auto_now=True)
    status = models.CharField(max_length=10,choices= STATUS_CHOICES, default= 'draft')
    class Meta:
        ordering= ('-publish',)

    def __str__(self):
        return self.title

    def  get_absolute_url(self):
        return reverse('blinder:post_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])

class Comment(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name=models.CharField(max_length=100)
    email=models.EmailField()
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    
    class Meta:
        ordering=('created',)
    
    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
