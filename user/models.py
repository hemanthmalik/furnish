from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60, default='')
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    mobileNo = models.CharField(max_length=10, unique=True)
    address = models.CharField(max_length=200, default='')

    USERNAME_FIELD = 'mobileNo'
    REQUIRED_FIELDS = ['first_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.mobileNo