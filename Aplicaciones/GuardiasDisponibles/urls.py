from django.urls import path, re_path

from . import views

app_name = "GuardiasDisponibles_app"

urlpatterns = [
    path('disponibles', views.indexView.as_view(), name = "disponibles"),
    re_path(r'^asignar/(?P<slug>[\w]+)/$', views.asignar, name='asignar')
]