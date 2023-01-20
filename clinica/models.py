from django.db import models
from django.core.exceptions import ValidationError
from datetime import date
from django.contrib.auth.models import User

class Especialidade(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Medico(models.Model):
    nome = models.CharField(max_length=255)
    crm = models.CharField(max_length=7)
    email = models.CharField(max_length=255)
    telefone = models.CharField(max_length=11)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

def validar_dia(value):
    today = date.today()
    weekday = date.fromisoformat(f'{value}').weekday()

    if value < today:
        raise ValidationError('Escolha uma data futura.')
    if (weekday == 5) or (weekday == 6):
        raise ValidationError('Escolha um dia útil (Segunda a Sexta).')

class Agenda(models.Model):
    HORARIOS = (
        ('8 as 10h', '8:00 as 10:00'),
        ('10 as 12h', '10:00 as 12:00'),
        ('14 as 17h', '14:00 as 17:00'),
        ('17 as 19h', '17:00 as 19:00'),
    )
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    hora = models.CharField(max_length=20, choices=HORARIOS, blank=False, null=False, default='1')
    data = models.DateField(help_text="Insira a data desejada.", validators=[validar_dia])

    class Meta:
        unique_together = ('data', 'hora')

    def __str__(self):
        return f'{self.medico}: {self.data.strftime("%d/%b/%Y")} - {self.hora}'

class Cliente(models.Model):
    SEXO = (
        ('M', 'Masculino'),
        ('F', 'Feminino')
    )
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11)
    email = models.CharField(max_length=255)
    telefone = models.CharField(max_length=11)
    sexo = models.CharField(max_length=1, choices=SEXO, blank=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    # user = models.OneToOneField(
    #     settings.AUTH_USER_MODEL, 
    #     verbose_name='Usuário', 
    #     on_delete=models.CASCADE
    # )

    def __str__(self):
        return self.nome


class Consulta(models.Model):
    cliente  = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    agenda_medico = models.OneToOneField(Agenda, on_delete=models.CASCADE)

    # This is a list of lists that must be unique when considered together.
    # It’s used in the Django admin and is enforced at the database level 
    # i.e., the appropriate UNIQUE statements are included in 
    # the CREATE TABLE statement).

    class Meta:
        unique_together = ('cliente', 'agenda_medico')

    def __str__(self):
        return f'{self.cliente}'




