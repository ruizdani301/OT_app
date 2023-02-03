from django.db import models

class User(models.Model):
    id_user = models.IntegerField(primary_key=True, blank=False, verbose_name='Cedula')
    name = models.CharField(max_length=20, blank=False, null=False, verbose_name='Nombre')
    last_name = models.CharField(max_length=30, blank=False, null=False, verbose_name='Apellido')
    username = models.CharField(max_length=30, blank=False, null=False, unique=True, verbose_name='Usuario')
    password = models.CharField(max_length=10, blank=False, verbose_name='Contraseña')
    job = models.CharField(max_length=25, blank=False, null=False, verbose_name='Cargo')

    def __str__(self):
        return f'{self.id_user}, {self.name}, {self.job}'


class Ot(models.Model):
    id_ot = models.CharField(max_length=10, unique=True, blank=False, null=False, verbose_name='OT')
    cod_sap = models.CharField(max_length=10, unique=True, blank=False, null=False,  verbose_name='CODIGO_SAP')
    description = models.CharField(max_length=300, null=False, verbose_name='Descripcción')
    location = models.CharField(max_length=300, blank=False, null=False, verbose_name='Ubicación')
    start = models.DateTimeField(auto_now=False, editable=True, verbose_name='Inicio')
    completed = models.DateTimeField(auto_now=False, editable=True, verbose_name='Finalizado')
    user_id = models.ForeignKey(User, related_name='user_ot', null=True,
                                on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id_ot}, {self.start}, {self.completed}'