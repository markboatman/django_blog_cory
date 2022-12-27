from django.shortcuts import render, redirect
from django.contrib import messages
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
      messages.success(request, f'Account created for {username}')
      return redirect('blog-home')
    
  else:
    form = UserRegistrationForm()
  # pass the form to the template, this passed dictionary is the context
  return render(request, 'users/register.html', {'form': form})


