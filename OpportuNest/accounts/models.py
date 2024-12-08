from cloudinary.models import CloudinaryField
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

    @property
    def is_company(self):
        return hasattr(self, 'company')

    @property
    def is_seeker(self):
        return hasattr(self, 'seeker')

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
        null=True,
        blank=True,
    )
    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.company_name


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
        null=True,
        blank=True
    )
    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )
    skills = models.ManyToManyField(
        to='skill.Skill',
    )
    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
    )


    def full_name(self):
        return f'{self.first_name} {self.last_name}'


    def __str__(self):
        return f'{self.first_name} {self.last_name}'