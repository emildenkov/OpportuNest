from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_welcome_email(recipient_email):
    subject = "Welcome to OpportuNest!"
    message = "Thank you for choosing us. We're excited to have you onboard!"

    send_mail(
        subject,
        message,
        settings.COMPANY_EMAIL,
        [recipient_email],
        fail_silently=True,
    )
