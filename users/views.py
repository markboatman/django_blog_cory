from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from this module or app
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
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
      return redirect('login')
    
  else:
    form = UserRegistrationForm()
  # pass the form to the template, this passed dictionary is the context
  return render(request, 'users/register.html', {'form': form})

# With this decorator, if the user is not logged in, they will be redirected to
# to accounts/login. That is the default. Change this in settings.py by setting:
# LOGIN_REDIRECT_URL='blog-home'
@login_required 
def profile(request):
  if request.method == 'POST':
    # could delete old image with this information. would have to compare
    # to the new image.url at request.POST or request.FILES
    print('profile view, user.profile.image.url is: %s' % request.user.profile.image.url)
    user_form = UserUpdateForm(request.POST, instance=request.user)
    profile_form = ProfileUpdateForm(request.POST, 
                                      request.FILES, 
                                      instance=request.user.profile)
    if user_form.is_valid() and profile_form.is_valid():
      print("user_form and profile_form are valid")
      user_form.save()
      profile_form.save()
      messages.success(request, f'Your profile has been updated!')
      return redirect('profile')
  else:
    user_form = UserUpdateForm(instance=request.user)
    profile_form = ProfileUpdateForm(instance=request.user.profile)

  context = {
    'user_form': user_form,
    'profile_form': profile_form,
  }
  return render(request, 'users/profile.html', context)
