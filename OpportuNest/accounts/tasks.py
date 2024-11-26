from celery import shared_task
from django.core.mail import send_mail
from OpportuNest import settings


@shared_task
def send_mail_upon_registration(email):
    subject = 'Welcome to OpportuNest'
    message = 'Thank you for choosing us.'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)