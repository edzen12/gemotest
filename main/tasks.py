from gemotest.celery import app
from django.core.mail import send_mail
from django.core.mail import EmailMessage


@app.task
def send_message(email, pdf):
    send = EmailMessage(
        'test',
        '',
        'gemotest.info.result@gmail.com',
        [email],
    )
    send.attach_file(pdf)
    send.send()