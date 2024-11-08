from django.db import models


class Job(models.Model):
    title = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )
    description = models.TextField(
        null=False,
        blank=False,
    )
    requirements = models.TextField(
        null=False,
        blank=False,
    )
    location = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )
    company = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )
    posted_by = models.ForeignKey(
        to='accounts.AppUser',
        on_delete=models.CASCADE,
        related_name='jobs',
    )
    date_posted = models.DateTimeField(
        auto_now_add=True,
    )