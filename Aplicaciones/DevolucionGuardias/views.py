from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


from ..Agenda.models import Guardia, User

class indexView(LoginRequiredMixin, ListView):
    login_url = '/login'
    redirect_field_name = 'redirect_to'
    template_name = "devolucion.html"
    context_object_name = "DevolucionGuardias"

    def get_queryset(self):
        return Guardia.object.filter(usuario = (User.objects.get(username = self.kwargs['userid'])))

def devolver(request, guardiaId):
    Guardia.object.filter(id = guardiaId).update(usuario = 1)
    return redirect('/disponibles')

def ir_a_devolver(request):
    userId = request.user
    return redirect('/devolucion/{}'.format(userId))