from django.db import models
from django.contrib.auth.models import User

# Create your models here.  
class Blog(models.Model):
  ID = models.BigAutoField(auto_created = True, primary_key=True, verbose_name="ID")
  title = models.CharField(max_length=200)
  content = models.TextField()
  author = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
  created_at = models.DateTimeField(auto_now_add=True, blank=True)
  updated_at = models.DateTimeField(auto_now=True)
  

class Comment(models.Model):
  ID = models.BigAutoField(auto_created = True, primary_key=True, verbose_name="ID")
  content = models.TextField()
  user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
  blog = models.ForeignKey(Blog, on_delete=models.CASCADE, blank=False)
  created_at = models.DateTimeField(auto_now_add=True, blank=True)
  updated_at = models.DateTimeField(auto_now=True)  