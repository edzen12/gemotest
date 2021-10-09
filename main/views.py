from django import forms
from django.shortcuts import render, redirect
from django.conf import settings
from main.forms import GemotestForm

from .models import Gemotest
from .tasks import send_message

import os
import pdfkit


def index(request):
    form = GemotestForm(request.POST, None)
    if form.is_valid():
        gemotest = Gemotest()
        gemotest.first_name = form.cleaned_data['first_name']
        gemotest.last_name = form.cleaned_data['last_name']
        gemotest.surname = form.cleaned_data['surname']
        gemotest.number_of_phone = form.cleaned_data['number_of_phone']
        gemotest.email = form.cleaned_data['email']
        gemotest.date_of_birth = form.cleaned_data['date_of_birth']
        gemotest.number_of_passport = form.cleaned_data['number_of_passport']
        gemotest.address = form.cleaned_data['address']
        gemotest.date_of_give_bio = form.cleaned_data['date_of_give_bio']
        gemotest.date_completed = form.cleaned_data['date_completed']
        gemotest.save()

        ida = gemotest.id
        pdf = pdfkit.from_url('http://89.223.71.86/rew/{id}/'.format(id=ida),
                              'pdf/sending-{id}.pdf'.format(id=ida))
        file_to_send = 'pdf/sending-{id}.pdf'.format(id=ida)
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