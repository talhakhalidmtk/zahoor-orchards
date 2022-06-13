from django.contrib import admin
from admin_panel.models import Client, Property, Agent, File

# Register your models here.
admin.site.register(Client)
admin.site.register(Property)
admin.site.register(File)
admin.site.register(Agent)


