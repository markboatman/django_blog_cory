from django.shortcuts import render
from django.views.generic import (
  ListView, 
  DetailView, 
  CreateView,
  UpdateView,
  DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# from the models file in the current package?
from .models import Post

def home(request):
  context = {
    'title': 'Home',
    'posts': Post.objects.all(),
  }
  # render() returns an HttpResponse or an exception
  return render(request, 'blog/home.html', context)

class PostListView(ListView):
  # list will be based on this model/table data
  model = Post
  template_name = 'blog/home.html' # default: <app>/<model>_<view_type>.html
  # override default value for context_object_name = 'object_list'
  context_object_name = 'posts'
  # set to list/array of ordering criteria, '-' reverse of chronilogically
  ordering = ['-date_posted']

class PostDetailView(DetailView):
  # will use all defaults names for template and context_object_name
  model = Post
  # create a view here: <app>/<model>_<view_type>.html so
  # blog/templates/blog/post_detail.html
class PostCreateView(LoginRequiredMixin, CreateView):
  # will use all defaults names for template and context_object_name
  model = Post
  fields = ['title', 'content']
  # we are setting the success redirect with Post. get_absolute_url()
  # but could set this attribute instead, did not test this
  # success_url = 'home/'
  # expects template at <app>/<model>_form.html
  def form_valid(self, form):
    # Post model has an author field, need to fill it out
    form.instance.author = self.request.user
    return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
  # will use all defaults names for template and context_object_name
  model = Post
  fields = ['title', 'content']
  # we are setting the success redirect in the model Post.get_absolute_url()
    # but could set this attribute instead, did not test this
  # success_url = 'home/'
  # expects template at <app>/<model>_form.html
  # allow them to change the author?
  def form_valid(self, form):
    # Post model has an author field, need to fill it out
    form.instance.author = self.request.user
    return super().form_valid(form)
  # this needs to be defined and will run because we inherited 
  # from UserPassesTest
  def test_func(self):
    # UpdateView makes get_object available, returns the current post
    post = self.get_object()
    if self.request.user == post.author:
      # User passes test
      return True
    # User fails test  
    return False   

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
  # will use all defaults names for template and context_object_name
  model = Post
  # 'home/' expands to post/3/home, must be '/home/' or '/'
  success_url = '/home/'
  # expects template here: <app>/<model>_confirm_delete.html
  # We overide the UserPassesTestMixin member method test_func()
  def test_func(self):
    # DeleteView makes get_object available, returns the current post
    post = self.get_object()
    if self.request.user == post.author:
      # User passes test
      return True
    # User fails test  
    return False  

def about(request):
  return  render(request, 'blog/about.html', {'title': 'About'})


