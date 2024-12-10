from cloudinary.models import CloudinaryField
from django.db import models
from OpportuNest.application.validators import PDFValidator


class Application(models.Model):
    job = models.ForeignKey(
        to='job.Job',
        on_delete=models.CASCADE,
        related_name='job_applications',
    )

    applicant = models.ForeignKey(
        to='accounts.AppUser',
        on_delete=models.CASCADE,
        related_name='applications',
    )

    resume = CloudinaryField(
        'file',
        resource_type='raw',
        folder='applications/resumes',
        validators=[
            PDFValidator()
        ],
        null=False,
        blank=False,
    )

    cover_letter = models.TextField(
        blank=False,
        null=False,
    )

    status = models.CharField(
        max_length=10,
        null=True,
        blank=True,
    )

    date_applied = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"Application from {self.applicant} for {self.job.title}"