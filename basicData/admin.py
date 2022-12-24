from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import *

class AdminMain(admin.ModelAdmin):
    list_display = ["code","name"]
class AdminSub(admin.ModelAdmin):
        list_display = ["code","name"]
class AdminDivide(admin.ModelAdmin):
        list_display = ["code","name"]
class AdminGood(admin.ModelAdmin):
        list_display = ["code","name","group","mainGroup"]        

admin.site.register(GoodsMainGroup,AdminMain)
admin.site.register(GoodsSubGroup,AdminSub)
admin.site.register(GoodsDivideGroup,AdminDivide)
admin.site.register(Good,AdminGood)
admin.site.register(Dc)
admin.site.register(Barache)
admin.site.register(DistrictManager)
admin.site.register(Manager)
admin.site.register(SaleLine)
admin.site.register(CostumersActivity)




