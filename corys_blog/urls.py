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
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('register/', user_views.register,  name='register'),
    # These are django class based views. They give us the forms and logic
    # but we have to build the templates
    # On successful login, django default is to go to /acounts/profile
    # Need to define the variable LOGIN_REDIRECT_URL='blog-home' to change default
   
    path('profile/', user_views.profile,  name='profile'),
    # paths/routes for django.contrib.auth imported views
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'),  name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'),  name='logout'),
    # for password reset functionality, django Password views expect the names
    # to be these. i.e. password_blah_blah
    path(
      'password-reset/', 
      auth_views.PasswordResetView.as_view(template_name='users/password-reset.html'),  
      name='password_reset'
    ),
    path(
      'password-reset/done/', 
      auth_views.PasswordResetDoneView.as_view(template_name='users/password-reset-done.html'),  
      name='password_reset_done'
    ),
    path(
      'password-reset-confirm/<uidb64>/<token>/', 
      auth_views.PasswordResetConfirmView.as_view(template_name='users/password-reset-confirm.html'),  
      # django PasswordResetView expects a name of 'password-reset_confirm
      name='password_reset_confirm'
    ),
    path(
      'password-reset-complete/', 
      auth_views.PasswordResetCompleteView.as_view(template_name='users/password-reset-complete.html'),  
      # django PasswordResetView expects a name of 'password_reset_confirm
      name='password_reset_complete'
    ),
    # include blog/specific paths/routes
    path('', include('blog.urls')),  # blog.urls is a file location identifier
    # Above will pull off blog/ because it matches
    # and pass '' as the url
    # this will match :8000/'' and go to blog/'' 
    # typing :8000/blog/ will not work anymore
] 

# if in dev environment
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)