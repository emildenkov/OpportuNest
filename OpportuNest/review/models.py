from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from OpportuNest.review.authentication import get_deleted_user


class Review(models.Model):
    company = models.ForeignKey(
        to='company_profile.CompanyProfile',
        on_delete=models.CASCADE,
        related_name='company_reviews'
    )
    reviewer = models.ForeignKey(
        to='accounts.User',
        on_delete= models.SET(get_deleted_user),
        related_name='reviews'
    )
    rating = models.IntegerField(
        blank=False,
        null=False,
        validators=[
            MaxValueValidator(5, 'Max rating is 5'),
            MinValueValidator(1, 'Minimum rating is 1'),
        ],
        default=0
    )
    date_posted = models.DateTimeField(
        auto_now_add=True,
    )