from django.http import Http404
from django.shortcuts import render, redirect
from .models import Patients, Todos, Consult
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
        todos = Todos.objects.all()
        consults = Consult.objects.filter(patient=patient)
        return render(request, 'patient.html', {'patient': patient, 'todos': todos, 'consults': consults})
    else:
        humor = request.POST.get('humor')
        geral_register = request.POST.get('geral_register')
        video = request.FILES.get('video')
        todos = request.POST.getlist('todos')

        consults = Consult(
            humor=int(humor),
            geral_register=geral_register,
            video=video,
            patient=patient
        )
        consults.save()

        for t in todos:
            todo = Todos.objects.get(id=t)
            consults.todo.add(todo)

        consults.save()
         
        messages.add_message(request, constants.SUCCESS, 'Registro de consulta adicionado com sucesso.')
        return redirect(f'/patients/{id}')

def upgrade_patient(request, id):
    payments_status = request.POST.get('payments_status')
    patient = Patients.objects.get(id=id)
    status = True if payments_status == 'ativo' else False
    patient.payments_status = status
    patient.save()

    return redirect(f'/patients/{id}')

def delete_consult(request, id):
    consult = Consult.objects.get(id=id)
    consult.delete()
    return redirect(f'/patients/{consult.patient.id}')

def public_consult(request, id):
    consults = Consult.objects.get(id=id)
    print(consults.link_publico)
    if not consults.patient.payments_status:
        raise Http404()
    return render(request, 'public_consult.html', {'consults': consults})
