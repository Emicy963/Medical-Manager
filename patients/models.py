from django.db import models

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

