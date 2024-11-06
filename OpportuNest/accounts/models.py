from django.contrib.auth.models import AbstractUser
from django.db import models

from OpportuNest.accounts.choices import UserChoices


class User(AbstractUser):
    user_type = models.CharField(
        max_length=20,
        choices= UserChoices.choices,
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.username