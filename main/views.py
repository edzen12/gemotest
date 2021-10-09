from django.shortcuts import render, redirect
from django.conf import settings

from .models import Gemotest
from .tasks import send_message

import os
import pdfkit


def index(request):
    if request.method == 'POST':
        first_name = request.POST.get('name')
        last_name = request.POST.get('last_name')
        surname = request.POST.get('surname')
        number_of_phone = request.POST.get('number_of_phone')
        email = request.POST.get('email')
        date_of_birth = request.POST.get('date_of_birth')
        number_of_passport = request.POST.get('number_of_passport')
        address = request.POST.get('address')
        date_of_give_bio = request.POST.get('date_of_give_bio')
        date_completed = request.POST.get('date_completed')
        gemotest = Gemotest.objects.create(first_name=first_name, last_name=last_name, surname=surname,
                                           number_of_phone=number_of_phone, date_of_birth=date_of_birth, email=email,
                                           number_of_passport=number_of_passport, address=address,
                                           date_of_give_bio=date_of_give_bio, date_completed=date_completed,
                                           )

        ida = gemotest.id
        pdf = pdfkit.from_url('http://127.0.0.1:8000/rew/{id}'.format(id=ida),
                              'pdf/sending{id}.pdf'.format(id=ida))
        file_to_send = 'pdf/sending{id}.pdf'.format(id=ida)
        file_to_send = os.path.join(settings.BASE_DIR, file_to_send)
        send_message.delay(email, pdf=file_to_send)
        return redirect('reference/{id}'.format(id=ida))
    return render(request, 'anketa.html', locals())


def second_index(request, id):
    info = Gemotest.objects.get(id=id)
    return render(request, 'secondList.html', locals())


def rew(request, id):
    obj = Gemotest.objects.get(id=id)
    return render(request, 'index_sending.html', locals())