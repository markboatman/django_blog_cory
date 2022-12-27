from django.shortcuts import render
# from the models file in the current package?
from .models import Post
posts = [
  {
    'author': 'Mark Boatman',
    'title': 'Marks blog post 1',
    'content': 'This is my most bestest post1',
    'date_posted': 'Dec 26, 2022',
  },
    {
    'author': 'Fred Jones',
    'title': 'Freds blog post 1',
    'content': 'This is my most mo betta blog post',
    'date_posted': 'Dec 27, 2022',
  },
]


def home(request):
  context = {
    'title': 'Home',
    'posts': Post.objects.all(),
  }
  # render() returns an HttpResponse or an exception
  return render(request, 'blog/home.html', context)

def about(request):
  return  render(request, 'blog/about.html', {'title': 'About'})


