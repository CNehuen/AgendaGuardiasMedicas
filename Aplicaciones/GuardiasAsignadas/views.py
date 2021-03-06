from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import request

from ..Agenda.models import Guardia, User

class indexView(LoginRequiredMixin, ListView):
    login_url = '/login'
    redirect_field_name = 'redirect_to'
    template_name = "Asignadas.html"
    context_object_name = "guardiasAsignadas"
    

    def get_queryset(self):
        return Guardia.object.filter(usuario = (User.objects.get(username = self.kwargs['userid'])))


def meAsignaron(request):
    userId = request.user
    return redirect('/asignadas/{}'.format(userId))