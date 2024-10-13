from django.core.mail import send_mail
from string import ascii_letters, digits
from random import choices



def send_email_confirm(url, email):
    send_mail(
        subject='Подтверждение регистрации',
        message=f'Для подтверждения регистрации пройдите по ссылке {url}',
        from_email=EMAIL_HOST_USER,
        recipient_list = [email],
        )


def send_email_reset_password(password, email):
    send_mail(
        subject="Сброс пароля",
        message=f"Новый пароль {password}",
        from_email=EMAIL_HOST_USER,
        recipient_list=[email],
    )

def generate_random_password():
    data = ascii_letters + digits
    return "".join(choices(data, k=8))