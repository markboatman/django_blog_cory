from django.urls import path
from .views import (
  PostListView, 
  PostDetailView, 
  PostCreateView,
  PostUpdateView,
  PostDeleteView,
  UserPostListView,
  )

from  . import views
# all these routes will be prefixed with blog/ in the browser
urlpatterns = [
  path('', PostListView.as_view(), name='blog-home'),
  path('home/', PostListView.as_view(), name='blog-home'),
  path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),

  # create url param for this route <pk> with a type of int, django class
  # views expect the url param to be <pk>
  path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
  path('post/new/', PostCreateView.as_view(), name='post-create'),
  path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
  path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
  path('about/', views.about, name='blog-about'),
]