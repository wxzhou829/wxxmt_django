from django.contrib import admin

# Register your models here.
from peijian.models import Supplier,Parts,Storage,Equi
class SupplierAdmin(admin.ModelAdmin):  
    list_display = ('name','address','contact','scope') 
admin.site.register(Supplier,SupplierAdmin)  

class PartsAdmin(admin.ModelAdmin):  
    list_display = ('p_id','name','standard','type','safe_num') 
admin.site.register(Parts,PartsAdmin)   

class StorageAdmin(admin.ModelAdmin):  
    list_display = ('date','part','supplier','price','in_num') 
admin.site.register(Storage,StorageAdmin)                           

admin.site.register(Equi)    

                          
from peijian.models import    Staff,Weixiu,Output                    
admin.site.register(Staff)  

class OutputInline(admin.TabularInline):
    model = Output
    extra = 2
    
class WeixiuAdmin(admin.ModelAdmin):  
    list_display = ('pline','equi','date_s','description','reason','method','date_e','date_n','staff','cost','finish')  
    list_filter = ['finish']
    inlines = [OutputInline]
admin.site.register(Weixiu,WeixiuAdmin)  

