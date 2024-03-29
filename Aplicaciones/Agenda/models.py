from django.db import models
from django.contrib.auth.models import User

class CentroSalud(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    departamento = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    telefono = models.IntegerField()
    emailSupervisor = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Medico(models.Model):
    ci = models.IntegerField(primary_key=True)
    ranking = models.IntegerField(default=0)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE,related_name='usuario')
    nroCaja = models.IntegerField()
    telefono = models.IntegerField()
    object = models.Manager()

    def __str__(self):
        return self.usuario



class Guardia(models.Model):
    id = models.IntegerField(primary_key=True)
    fecha = models.DateField()
    turno = models.CharField(max_length=25)
    centroSalud = models.ForeignKey(CentroSalud,on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.DO_NOTHING, blank = True, null = True)
    usuario = models.ForeignKey(User, default=1, on_delete=models.DO_NOTHING, blank = True, null = True)
    object = models.Manager()

    def __str__(self):
        return "{}) {} {} ({})".format(self.id, self.centroSalud, self.turno, self.fecha)


class Fecha(models.Model):
    fecha = models.DateField()

    def __str__(self):
        return str(self.fecha)