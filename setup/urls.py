from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from clinica import views
from clinica.views import ClientesViewSet, ConsultasViewSet, EspecialidadesViewSet, MedicosViewSet, AgendasViewSet
from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register('medicos', MedicosViewSet, basename='Medicos')
router.register('especialidades', EspecialidadesViewSet, basename='Especialidades')
router.register('clientes', ClientesViewSet, basename='Clientes')
router.register('consultas', ConsultasViewSet, basename='Consultas')
router.register('agendas', AgendasViewSet, basename='Agendas')

app_name = 'clinica'

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path("login", views.login_request, name="login"),
    path("register", views.register_request, name="register"),
    path("logout", views.logout_request, name= "logout"),
    path('agenda/', views.agenda, name='agenda'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
