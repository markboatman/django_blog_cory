from django.db import models
from django.contrib.auth.models import User
# from PIL import Image
# Profiles have 1 related user and users have 1 related profile
# Can create and assign profiles in /admin tool after registration and migration
# Have to register this Model in current_app/admin.py to see in admin/
class Profile(models.Model):
  # this is a foreign key
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  # this is member var that is set to an instance of an ImageField
  # We can use an ImageField because with installed Pillow
  # 'pip freeze' to see installation
  # image will contain the url/address of where the image was stored 
  # at image.url
  image = models.ImageField(default='default.jpg', upload_to='profile-pics')
  
  def __str__(self):
    return f'{self.user.username} Profile'


  # Can use an AWS Lamda funtion to replace this functionality on the AWS side
  # This save() is from before we started using AWS buckets
  # args - positional arguments, kwargs - keyword arguments
  # def save(self, *args, **kwargs): 
  #   # run parent save, this will save the profile pic to the filesystem
  #   super(Profile, self).save(*args, **kwargs)
  #   # resize the profile pic
  #   image = Image.open(self.image.path)
  #   if image.height > 300 or image.width > 300:
  #     # create a tuple of max sizes
  #     max_sizes = (300, 300)
  #     # resize image in place
  #     image.thumbnail(max_sizes)
  #     # save/overwrite the old big image
  #     image.save(self.image.path)



    

# Assign a profile to a user in the admin/ tool then do this 
# using 'PYTHON MANAGE.PY SHELL'
# from django.contrib.auth.models import User
# user =  User.objects.filter(username='mark').first()
# user
# user.profile
# user.profile.image
# user.profile.image.width
# user.profile.image.url
