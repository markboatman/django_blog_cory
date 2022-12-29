from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# inherit from UserCreationForm
class UserRegistrationForm(UserCreationForm):
  # add email field to UserCreationForm parent class
  # forms.EmailField(required=True), this is the default
  email = forms.EmailField()
  
  # nested namespace for configuration settings for this UserCreationForm
  # decendant
  class Meta:
    model = User
    # the fields that will be in the form
    fields = ['username', 'email', 'password1', 'password2']

# Create a form based on a model
class UserUpdateForm(forms.ModelForm):
  email = forms.EmailField()
  
  class Meta:
    model = User
    # the fields that will be in the form
    fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
  class Meta:
    # fields will come from the Profile model
    model = Profile
    # fields to present
    fields = ['image']