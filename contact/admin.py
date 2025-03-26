from django.contrib import admin
from contact.models import contact

class contactAdmin(admin.ModelAdmin):
    list_display=('name','phone','email','message')
admin.site.register(contact,contactAdmin)