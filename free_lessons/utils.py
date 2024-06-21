from django.core.mail import send_mail
from django.conf import settings


def send_message_email(user_email, subject, message):
    send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list=[user_email], fail_silently=False,)
