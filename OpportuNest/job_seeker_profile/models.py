from cloudinary.models import CloudinaryField
from django.db import models


class JobSeekerProfile(models.Model):
    user = models.OneToOneField(
        to='accounts.User',
        on_delete=models.CASCADE
    )
    skills = models.ManyToManyField(
        to='skill.Skill',
    )
    experience = models.TextField()
    profile_pic = CloudinaryField(
        'profile_pic'
    )