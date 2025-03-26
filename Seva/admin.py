from django.contrib import admin
from Seva.models import Seva

class SevaAdmin(admin.ModelAdmin):
    list_display=('Seva_title','Seva_desc')
admin.site.register(Seva,SevaAdmin)
