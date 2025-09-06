from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # We are extending Django's default User model.
    # The only change we're making is to ensure the email is unique,
    # which is standard practice for modern web apps.
    email = models.EmailField(unique=True)

    # We can add more fields later, like a profile picture or biography.
    
    def __str__(self):
        return self.username
