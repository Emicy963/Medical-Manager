from django.shortcuts import render
from django.http import HttpResponse

def patients(request):
    if request.method == 'GET':
        return render(request, 'patients.html')
