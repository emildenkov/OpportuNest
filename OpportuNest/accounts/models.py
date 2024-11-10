from cloudinary.models import CloudinaryField
from decouple import config
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from OpportuNest.accounts.managers import AppUserManager


class AppUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )

    is_active = models.BooleanField(
        default=True
    )

    is_staff = models.BooleanField(
        default=False
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = AppUserManager()



class Company(models.Model):
    company_name = models.CharField(
        max_length=100,
        unique=True,
        null=False,
        blank=False,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    logo = CloudinaryField(
        'logo',
        default=config('DEFAULT_COMPANY_IMAGE'),
        null=True,
        blank=True,
    )
    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
    )


class Seeker(models.Model):

    first_name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )
    last_name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )
    profile_picture = CloudinaryField(
        'profile_picture',
        default = config('DEFAULT_PROFILE_IMAGE'),
        null=True,
        blank=True
    )
    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )
    skills = models.ManyToManyField(
        to='skill.Skill'
    )
    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
    )

    def full_name(self):
        return f'{self.first_name} {self.last_name}'