from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Review(models.Model):
    reviewer = models.ForeignKey(
        to='accounts.AppUser',
        on_delete= models.CASCADE,
        related_name='reviews'
    )

    feedback = models.TextField()

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