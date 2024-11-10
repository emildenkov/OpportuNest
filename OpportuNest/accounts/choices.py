from django.db import models


class UserChoices(models.TextChoices):
    EMPLOYER = 'company', 'Register Company account.'
    JOB_SEEKER = 'seeker', 'Register Job Seeker account.'