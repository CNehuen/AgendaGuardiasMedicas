from django.contrib import admin


from .models import Medico, Guardia, CentroSalud

admin.site.register(Medico)
admin.site.register(Guardia)
admin.site.register(CentroSalud)
