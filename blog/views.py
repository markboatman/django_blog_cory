from django.shortcuts import render
# from the models file in the current package?
from .models import Post

def home(request):
  context = {
    'title': 'Home',
    'posts': Post.objects.all(),
  }
  # render() returns an HttpResponse or an exception
  return render(request, 'blog/home.html', context)

def about(request):
  return  render(request, 'blog/about.html', {'title': 'About'})


