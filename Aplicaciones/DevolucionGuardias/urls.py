from django.urls import path, re_path

from . import views

app_name = "DevolucionGuardias_app"

urlpatterns = [
    path ("devolverGuardia", views.ir_a_devolver),
    re_path(r'^devolucion/(?P<userid>[\w]+)/$', views.indexView.as_view(), name = "devolucion"),
    re_path(r'^devolver/(?P<guardiaId>[\w]+)/$', views.devolver, name = "devolver"),
]