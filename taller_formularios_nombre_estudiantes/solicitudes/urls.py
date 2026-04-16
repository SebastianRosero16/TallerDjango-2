from django.urls import path
from . import views

app_name = 'solicitudes'

urlpatterns = [
    path('', views.formulario_solicitud, name='formulario'),
    path('confirmacion/', views.confirmacion_solicitud, name='confirmacion'),
]
