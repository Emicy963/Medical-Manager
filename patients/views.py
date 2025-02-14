from django.shortcuts import render, redirect
from .models import Patients
from django.contrib import messages
from django.contrib.messages import constants

def patients(request):
    if request.method == 'GET':
        conditions = Patients.conditions_choices
        return render(request, 'patients.html', {'conditions': conditions})
    elif request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        conditions = request.POST['conditions']
        picture = request.FILES['picture']

        if len(name.strip()) == 0 or not picture:
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos!')
            return redirect('patients')
        
        patients = Patients(
            name=name,
            email=email,
            phone=phone,
            conditions=conditions,
            picture=picture,
        )

        patients.save()
        messages.add_message(request, constants.SUCCESS, 'Cadastro feito com sucesso!')
        return redirect('patients')

