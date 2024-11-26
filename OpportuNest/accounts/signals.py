from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from OpportuNest.accounts.tasks import send_mail_upon_registration

UserModel = get_user_model()

@receiver(post_save, sender=UserModel)
def send_notification_upon_registration(sender, instance, created, **kwargs):
    if created:
        send_mail_upon_registration.delay(
            instance.email
        )