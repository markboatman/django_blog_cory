from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from this module or app
from .forms import UserRegistrationForm
# messages.debug
# messages.success
# messages.warning
# messages.error
# messages.info

def register(request):
  if request.method == 'POST':
    # create a form with input values set from the POST request
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
      # form is of type UserCreationForm so save() will 
      # hash the password, and create a User model and save it to DB
      form.save()
      username = form.cleaned_data.get('username')
      # messages will be on the blog-home context
      messages.success(request, f'Your account has been created, please login.')
      return redirect('users-login')
    
  else:
    form = UserRegistrationForm()
  # pass the form to the template, this passed dictionary is the context
  return render(request, 'users/register.html', {'form': form})

# With this decorator, if the user is not logged in, they will be redirected to
# to accounts/login. That is the default. Change this in settings.py
# 
@login_required 
def profile(request):
  return render(request, 'users/profile.html')
