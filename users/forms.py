from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# inherit from UserCreationForm
class UserRegistrationForm(UserCreationForm):
  # forms.EmailField(required=True), this is the default
  email = forms.EmailField()
  
  # nested namespace for configuration settings for this UserCreationForm
  # decendant
  class Meta:
    model = User
    # the fields that will be in the form
    fields = ['username', 'email', 'password1', 'password2']



