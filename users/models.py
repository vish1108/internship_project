from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class CustomUserManager(UserManager):
    def get_by_natural_key(self, email):
        return self.get(email=email)


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]  # username still needed for admin

    objects = CustomUserManager()

    def __str__(self):
        return self.email
