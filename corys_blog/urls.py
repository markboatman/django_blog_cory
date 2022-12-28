"""corys_blog URL Configuration
** This is the PROJECT LEVEL URLS.PY file
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # blog.urls is a file location identifier
    # this will pull off blog/ because it matches
    # and pass '' as the url
    # path('blog/', include('blog.urls')),
    # this will match :8000/'' and go to blog/'' 
    # typing :8000/blog/ will not work anymore
    path('', include('blog.urls')),
    path('register/', user_views.register,  name='register'),
    # these are django class based views, give us the forms and logic
    # We have to build the templates
    # On successful login, django default is to go to /acounts/profile
    # Need to define the variable LOGIN_REDIRECT_URL='blog-home' to change default
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'),  name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'),  name='logout'),
    path('profile/', user_views.profile,  name='profile'),
    
]
