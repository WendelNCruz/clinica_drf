from django.views.generic.list import ListView
from rest_framework import viewsets
from clinica.models import Especialidade, Cliente, Consulta, Medico, Agenda
from clinica.serializer import ClientesSerializer, ConsultasSerializer, EspecialidadesSerializer, MedicosSerializer, AgendasSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from .forms import AgendaForm


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


from clinica.forms import NewUserForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


def homepage(request):
    return render(request, "clinica/home.html", {})

class ClientesViewSet(viewsets.ModelViewSet):
    """Exibir todos os Clientes"""
    queryset = Cliente.objects.all()
    serializer_class = ClientesSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ConsultasViewSet(viewsets.ModelViewSet):
    """Exibir todos as Consultas"""
    queryset = Consulta.objects.all()
    serializer_class = ConsultasSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class EspecialidadesViewSet(viewsets.ModelViewSet):
    """Exibir todos as Especialidades"""
    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadesSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class MedicosViewSet(viewsets.ModelViewSet):
    """Exibir todos as Medicos"""
    queryset = Medico.objects.all()
    serializer_class = MedicosSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class AgendasViewSet(viewsets.ModelViewSet):
    """Exibir todos as Medicos"""
    queryset = Agenda.objects.all()
    serializer_class = AgendasSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]



def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return render(request, "clinica/home.html", {})
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(
        request=request,
        template_name="clinica/register.html",
        context={"register_form": form},
    )


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return render(request, "clinica/home.html", {})
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(
        request=request,
        template_name="clinica/login.html",
        context={"login_form": form},
    )

def logout_request(request):
    logout(request)
    messages.info(request, "Voce esta deconectado.")
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return render(request, "clinica/home.html", {})
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(
        request=request,
        template_name="clinica/login.html",
        context={"login_form": form},
    )

def agenda(request):
    form = AgendaForm(request.POST)
    return render(request, 'clinica/consulta.html', {'form':form})

def user_detail(request):
   user_detail = User.objects.filter(id=id)
   return(request,'index.html',{'user_detail':user_detail})

class IniciView(ListView):
    template_name = 'clinica/index.html'
    model = User