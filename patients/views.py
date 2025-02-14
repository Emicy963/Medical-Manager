from django.shortcuts import render, redirect
from .models import Patients
from django.contrib import messages
from django.contrib.messages import constants

def patients(request):
    if request.method == 'GET':
        patients = Patients.objects.all()
        return render(request, 'patients.html', {'conditions': Patients.conditions_choices, 'patients': patients})
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

def patient_view(request, id):
    patient = Patients.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'patient.html', {'patient': patient})

def upgrade_patient(request, id):
    payments_status = request.POST.get('payments_status')
    patient = Patients.objects.get(id=id)
    status = True if payments_status == 'ativo' else False
    patient.payments_status = status
    patient.save()

    return redirect(f'/patients/{id}')
