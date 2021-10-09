from django.core.mail import EmailMessage

from gemotest.celery import app


@app.task
def send_message(email, pdf):
    send = EmailMessage(
        'Результаты анализов. Лаборатория Гемотест.',
        """
        Доброго времени суток! 
        Спасибо! Лаборатория Гемотест.
        """,
        'gemotest.info.result@gmail.com',
        [email],
    )
    send.attach_file(pdf)
    send.send()
