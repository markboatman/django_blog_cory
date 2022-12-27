from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
  title = models.CharField(max_length=100)
  # unrestricted text
  content = models.TextField()
  # possible values to DateTimeField constructor
  # auto_now_add = True - create time, cannot change,
  #  auto_now - last updated time
  # can change default=...
  date_posted = models.DateTimeField(default=timezone.now) 
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  # how to represent our self as a string
  # __method__ is a 'dunder' method
  def __str__(self):
    return self.title
