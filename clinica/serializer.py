from rest_framework import serializers
from clinica.models import Especialidade, Cliente, Consulta, Medico, Agenda


class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class ConsultasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = '__all__' 


class EspecialidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidade
        fields = '__all__' 


class MedicosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = '__all__' 


class AgendasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agenda
        fields = '__all__' 