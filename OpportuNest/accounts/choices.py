from django.db import models


class UserChoices(models.TextChoices):
    EMPLOYER = 'Employer', 'Employer'
    JOB_SEEKER = 'Job Seeker', 'Job Seeker'