from django.db import models
from django.urls import reverse

class Patients(models.Model):
    conditions_choices = {
        ('TDAH', 'TDAH'),
        ('D', 'Depressão'),
        ('A', 'Ansiedade'),
        ('TAG', 'Transtoono de ansiedade generalizada'),
    }

    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255, null=True, blank=True)
    picture = models.ImageField(upload_to='pictures')
    payments_status = models.BooleanField(default=True)
    conditions = models.CharField(max_length=4, choices=conditions_choices)

    def __str__(self):
        return self.name
    
class Todos(models.Model):
    choices_frequence = (
        ('D', 'Diário'),
        ('1S', '1 vez por semana'),
        ('2S', '2 vezes por semana'),
        ('3S', '3 vezes por semana'),
        ('N', 'Ao necessiatr')
    )
    todo = models.CharField(max_length=255)
    instrution = models.TextField()
    frequence = models.CharField(max_length=2, choices=choices_frequence, default='D')

    def __str__(self):
        return self.todo
    
class Consult(models.Model):
    humor = models.PositiveIntegerField()
    geral_register = models.TextField()
    video = models.FileField(upload_to='video')
    todo = models.ManyToManyField(Todos)
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.patient.name
    
    @property
    def link_publico(self):
        return f"http://127.0.0.1:8000{reverse('public_consult', kwargs={'id': self.id})}"
    