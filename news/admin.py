from django.contrib import admin
from news.models import news

class newsAdmin(admin.ModelAdmin):
    list_display=('news_title','news_desc')
admin.site.register(news,newsAdmin)

# Register your models here.
