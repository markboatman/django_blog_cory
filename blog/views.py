from django.shortcuts import render, get_object_or_404
from django.views.generic import (
  ListView, 
  DetailView, 
  CreateView,
  UpdateView,
  DeleteView
)
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# from the models file in the current package?
from .models import Post

def home(request):
  context = {
    'title': 'Home',
    'posts': Post.objects.all(),
    'user': request.user,
  }
  # render() returns an HttpResponse or an exception
  return render(request, 'blog/home.html', context)

# This is displayed on the home page
class PostListView(ListView):
  # list items will be based on this model/table data
  model = Post
  # default template name would be based on this:
  #  <app>/<model>_<view_type>.html = blog/post_list.html
  # override the default template name.
  template_name = 'blog/home.html' 
  # default for context_object_name - context_object_name = 'object_list'
  # override default, my object_list is a list of posts
  context_object_name = 'posts'
  # set  the 'object_list' ordering criteria, '-' reverse of chronilogically
  ordering = ['-date_posted']
  paginate_by = 5

# This list is specific to a user, using PAGNATION here
class UserPostListView(ListView):
  # list will be based on this model/table data
  model = Post
  # default template_name =  <app>/<model>_<view_type>.html
  # override
  template_name = 'blog/user_posts.html' 
  # override default value for context_object_name = 'object_list'
  context_object_name = 'posts'
  # if we override get_queryset() below, 'ordering=' is ignored
  # ordering = ['-date_posted'] 
  paginate_by = 5

  # override inherited method so we can filter
  # I.E. filter the posts by author.username
  def get_queryset(self):
    # self.kwargs.get('username') returns the value at '?username=fred', i.e 'fred'
    # if user not found go to a 404 page
    user = get_object_or_404(User, username=self.kwargs.get('username'))
    return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
  # we will create template and use a context_object_name(d) with
  # default names values
  model = Post
  # create a view here: <app>/<model>_<view_type>.html so
  # blog/templates/blog/post_detail.html
  # context_object_name will be 'object_list' by defaut

class PostCreateView(LoginRequiredMixin, CreateView):
  model = Post
  # input fields
  fields = ['title', 'content']
  # we are setting the success redirect with Post. get_absolute_url()
  # but could set this attribute instead, did not test this
  # success_url = 'home/'
  # expects template at <app>/<model>_form.html so blog/post_form.html
  def form_valid(self, form):
    # Post model has an author field, need to give it a value
    form.instance.author = self.request.user
    return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
  # will use defaults names for template and context_object_name
  model = Post
  fields = ['title', 'content']
  # we are setting the success redirect in the model Post.get_absolute_url()
    # but could set this attribute instead, did not test this
  # success_url = 'home/'
  # expects template at <app>/<model>_form.html
  def form_valid(self, form):
    # Post model has an author field, need to fill it out
    form.instance.author = self.request.user
    # now let the parent handle the validation
    return super().form_valid(form)
  # this needs to be defined/overridden? and will run because we inherited it
  # from UserPassesTestMixin
  def test_func(self):
    # UpdateView makes get_object available, returns the current post
    post = self.get_object()
    if self.request.user == post.author:
      # User passes test
      return True
    # User fails test, don't know how this error would propagate?
    return False   

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
  # will use defaults names for template_name and context_object_name
  model = Post
  # 'home/' causes ERROR expands to post/3/home, must be '/home/' or '/'
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


