from django.contrib import admin
from .models import *

class AdminPorsantGroup(admin.ModelAdmin):
    list_display = ["id","center","month","year","qnty","groupList"]
    list_editable = ["center","month","year"]
admin.site.register(PorsatnGroup,AdminPorsantGroup)
class AdminSalerTarget(admin.ModelAdmin):
    list_display = ["id","saler","month","year","qnty"]
    list_editable = ["saler","month","year"]
admin.site.register(SalerTargets,AdminSalerTarget)