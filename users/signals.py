from django.db.models.signals import post_save
# User will send the post_save signal
from django.contrib.auth.models import User
# This function will receive the post_save signal
from django.dispatch import receiver
from .models import Profile

# We want a new profile for each created user
# Decorator logic, when a User is saved, listen for post_save signal and its associated
# data. Then execute create_profile with the post_save signals associated data (arguments
# to create_profile)
# create_profile will be the receiver function
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs): # kwargs are optional args
  if created:
    Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
  # save the user's profile on post_save of the User
  instance.profile.save()
