from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

from django.dispatch import receiver
from .tasks import send_welcome_email

UserModel = get_user_model()

@receiver(post_save, sender=UserModel)
def user_created_signal(sender, instance, created, **kwargs):
    if created:
        send_welcome_email.delay(instance.email)
