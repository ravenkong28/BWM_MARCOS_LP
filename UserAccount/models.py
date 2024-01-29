from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.core.validators import FileExtensionValidator

class ProfileModel(models.Model):
     user = models.OneToOneField(User, on_delete=models.CASCADE)
     image = models.ImageField(default='default.jpg', upload_to='profile', validators=[
                                   FileExtensionValidator(['png', 'jpg', 'jpeg'])])

     def __str__(self):
          return self.user.username