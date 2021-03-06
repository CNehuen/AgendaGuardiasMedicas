from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from ..Agenda.models import Medico


class indexView(TemplateView):
    template_name = "login.html"
