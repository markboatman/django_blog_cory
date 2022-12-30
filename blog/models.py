from django.db import models
from django.utils import timezone
from django.urls import reverse
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

  # django needs this to know where to go after successful creation of
  # a post
  def get_absolute_url(self):
    # reverse will get the url based on the django name for the route
    # and then render the route
    return reverse('post-detail', kwargs={'pk': self.pk})
