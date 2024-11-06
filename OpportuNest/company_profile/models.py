from cloudinary.models import CloudinaryField
from django.db import models


class CompanyProfile(models.Model):
    user = models.OneToOneField(
        to='accounts.User',
        on_delete=models.CASCADE
    )
    company_name = models.CharField(
        max_length=75,
    )
    website = models.URLField()
    description = models.TextField()
    logo = CloudinaryField('company_logo')