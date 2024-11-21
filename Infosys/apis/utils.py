from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMessage


def send_email_notification(subject, message, recipient_email):
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[recipient_email],
        fail_silently=False,
    )

def send_html_email_notification(subject, message, recipient_email):
    """
    Sends an HTML email notification.
    """
    context = {'subject': subject, 'message': message}
    html_message = render_to_string('emails/leave_notification.html', context)
    email = EmailMessage(subject, html_message, settings.EMAIL_HOST_USER, [recipient_email])
    email.content_subtype = 'html'
    email.send()
