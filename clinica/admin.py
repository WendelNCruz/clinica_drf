from django.contrib import admin
from clinica.models import Especialidade, Medico, Agenda, Cliente, Consulta

class Especialidades(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    list_per_page = 20

admin.site.register(Especialidade, Especialidades)

class Medicos(admin.ModelAdmin):
    list_display = ('id', 'nome','crm', 'email', 'telefone', 'especialidade')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20

admin.site.register(Medico, Medicos)

class Agendas(admin.ModelAdmin):
    list_display = ('id', 'medico','hora', 'data')
    list_display_links = ('id', 'medico')
    search_fields = ('medico',)

admin.site.register(Agenda, Agendas)

class Clientes(admin.ModelAdmin):
    list_display = ('id','nome', 'cpf', 'email', 'telefone', 'sexo')
    exclude = ('user',)
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20

admin.site.register(Cliente, Clientes)


class Consultas(admin.ModelAdmin):
    list_display = ('id','cliente', 'agenda_medico')
    list_display_links = ('id', 'cliente')
    search_fields = ('cliente',)
    list_per_page = 10

admin.site.register(Consulta, Consultas)