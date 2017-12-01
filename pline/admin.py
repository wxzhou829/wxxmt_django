from django.contrib import admin

# Register your models here.
from pline.models import JiBen,GuZhang,Yao,JiaPD3,JiaPG2,JiaPG3,Cost,CostMonth

#基本信息表
class GuZhangInline(admin.TabularInline):
    model = GuZhang
    extra = 1
    
class YaoInline(admin.TabularInline):
    model = Yao
    extra = 2
    
class JiBenAdmin(admin.ModelAdmin):
    list_display = ('pline', 'date', 'trl', 'clmj','yygs','amp','shui','dian','bl')
    list_filter = ['pline']
    fieldsets = [
        (None,               {'fields': [('pline','date')]}),
        ('基本数据', {'fields': [('kjcs', 'scss','trl'),('clmj','yygs','amp'),('shui','dian','bl')]}),
        ('未稼动', {'fields': [('ddw', 'cfw','dqw'),('wcw','qtw')], 'classes': ['collapse']}),
        ('不良杆数', {'fields': [('scy', 'sc_count'),('mhy','mh_count'),('csy', 'cs_count'),('qpy','qp_count'),('cty', 'ct_count'),('qty','qt_count')],'classes': ['collapse']}),
     ]
    inlines = [GuZhangInline,YaoInline]
   
admin.site.register(JiBen, JiBenAdmin)   

#PD3加药
class JiaPD3Admin(admin.ModelAdmin):
    list_display = ("date",'ct','cd','cdpj','dj','djpj','ys','xb', 'lj','nz98','nzfb','h0616y','hztzj','j124', 'j44s','j44h','j447s1','j447s2','j447s3','j447r3', 'j118n')
    #list_filter = ['date']
    fieldsets = [
        ('PD3',               {'fields': ['date']}),
        ('前处理', {'fields': [('ct', 'cd','cdpj'),('dj','djpj','ys')]}),
        ('电镀', {'fields': [('xb', 'lj','nz98'),('nzfb','h0616y','hztzj')]}),
        ('钝化', {'fields': [('j124', 'j44s','j44h'),('j447s1','j447s2','j447s3'),('j447r3', 'j118n')]}),
     ]
admin.site.register(JiaPD3,JiaPD3Admin)  

#PG2加药
class JiaPG2Admin(admin.ModelAdmin):
    list_display = ("date",'sc30', 'hcl','rc30','rc25st','ds31','naoh','j441a', 'j444cs','j444cst','j447md1','j447md2','j447md3','j447md4','j447md7','j118')
    fieldsets = [
        ('PG2',               {'fields': ['date']}),
        ('前处理', {'fields': [('sc30', 'hcl','rc30'),('rc25st','ds31','naoh')]}),
        ('电镀', {'fields': [('xb', 'lj','nz200r'),('nzrba','h0616y','hztzj')]}),
        ('钝化', {'fields': [('j441a', 'j444cs','j444cst'),('j447md1','j447md2','j447md3'),('j447md4','j447md7','j118')]}),
     ]
admin.site.register(JiaPG2,JiaPG2Admin)  

#PG3加药
class JiaPG3Admin(admin.ModelAdmin):
    list_display = ("date",'sc30', 'hcl','rc30','rc25st','sm','naoh','j441a', 'j444cs','j444cst')
    fieldsets = [
        ('PG3',               {'fields': ['date']}),
        ('前处理', {'fields': [('sc30', 'hcl','rc30'),('rc25st','sm','naoh')]}),
        ('电镀', {'fields': [('xb', 'lj','nz200r'),('nzrba','h0616y','hztzj')]}),
        ('钝化', {'fields': [('j441a', 'j444cs','j444cst')]}),
     ]
admin.site.register(JiaPG3,JiaPG3Admin) 


#其他费用
class CostAdmin(admin.ModelAdmin):
    list_display = ("o_date",'jbss', 'jbxs','sbyl','sdj','wsf','qbyl','qdj', 'lbf',
                'bzf','bgf','dzyh','wlxh','other')
    fieldsets = [
        (None,               {'fields': ['o_date']}),
        ('其他费用输入', {'fields': [('jbss', 'jbxs'),('sbyl','sdj','wsf'),('qbyl','qdj', 'lbf','bzf'),('bgf','dzyh','wlxh','other')]}),
     ]
admin.site.register(Cost,CostAdmin) 

#其他费用(月)
class CostMonthAdmin(admin.ModelAdmin):
    list_display = ('o_date', 'jbf','sf','zqf', 'lbf','bzf','bgf','dzyh','wlxh','other')
    fieldsets = [
        (None,               {'fields': ['o_date']}),
        ('其他费用输入', {'fields': [('jbf','sf','zqf'), ('lbf','bzf','bgf'),('dzyh','wlxh','other')]}),
     ]
admin.site.register(CostMonth,CostMonthAdmin) 

#最大面积
from pline.models import MaxMJ
class MaxMJAdmin(admin.ModelAdmin):
    list_display = ('pline','yao','maxV')
admin.site.register(MaxMJ,MaxMJAdmin) 

#全检数据
from pline.models import Quanjian , Quandata
class QuanjianAdmin(admin.ModelAdmin):  
    list_display = ('customer','jianming','jianhao')                   
admin.site.register(Quanjian,QuanjianAdmin)   
class QuandataAdmin(admin.ModelAdmin):  
    list_display = ('date','quanjian','total')          
admin.site.register(Quandata, QuandataAdmin) 

#水表
from pline.models import Water, JianYu,JianTime
class WaterAdmin(admin.ModelAdmin):  
    list_display = ('date','main_water','main_water_n')          
admin.site.register(Water, WaterAdmin)

class JianYuAdmin(admin.ModelAdmin):
    list_display =('name','mianji')
admin.site.register(JianYu,JianYuAdmin)

class JianTimeAdmin(admin.ModelAdmin):
    list_display =('jianyu','date')
    list_filter = ['jianyu']
admin.site.register(JianTime,JianTimeAdmin)
