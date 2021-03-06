from django.urls import path, re_path

from . import views

app_name = "GuardiasAsignadas_app"

urlpatterns = [
    re_path(r'^asignadas/(?P<userid>[\w]+)/$', views.indexView.as_view(), name = "asignadas"),
    path("meAsignaron", views.meAsignaron, name="meAsignaron")
]