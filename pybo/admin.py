from django.contrib import admin
from .models import News
# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(News, NewsAdmin)