from django.db import models

# Create your models here.

#定义供应商表
class Supplier(models.Model):
    name = models.CharField('名称',max_length=50)
    address = models.CharField('地址',max_length=80)
    contact = models.CharField('联系人/电话',max_length=50,  blank=True, null=True)
    scope= models.CharField('经营范围',max_length=100,  blank=True, null=True) 
   
    class Meta:
        verbose_name_plural = "供应商"   
        ordering = ["name"]
        
    def __str__(self):
        return self.name   
        
        
        
#定义配件表
class Parts(models.Model):
    p_id = models.CharField('编号',max_length=20, unique=True)     
    name = models.CharField('名称',max_length=50)
    standard = models.CharField('规格',max_length=50,null=True,blank=True)
    type = models.CharField('型号',max_length=50,null=True,blank=True)
    stock = models.IntegerField('库存', default=0) 
    safe_num = models.IntegerField('安全数',default=0)
    image = models.ImageField(upload_to='img',null=True)
    
    class Meta:
        verbose_name_plural = "配件表"   
        ordering = ["p_id"]
        
    def __str__(self):
        return self.p_id      
        
#定义入库表
class Storage(models.Model):
    date = models.DateField('日期')
    part = models.ForeignKey(Parts,on_delete=models.CASCADE,verbose_name='配件编号')
    supplier = models.ForeignKey(Supplier,on_delete=models.CASCADE,verbose_name='供应商')
    price = models.DecimalField('价格', max_digits=11, decimal_places=2,null=True,blank=True)
    in_num = models.IntegerField('数量')
    class Meta:
        verbose_name_plural = "入库表"   
        ordering = ["-date"]
  

Pline_choices = (
    ('4', 'PG2'),
    ('5', 'PD3'),
    ('6', 'PG3'),
    ('7', '其他'),
)  

Equi_choices =(
    ('295', '未纳入保养'),
    ('296', '保养不足'),
    ('297', '正常损耗'),
    ('298', '操作不当'),
    ('299', '5S改善'),
    ('300', '遗留问题'),
    ('301', '设计缺陷'),
    ('302', '维护保养'),
)

class Equi(models.Model):
    name = models.CharField('设备',max_length=20, unique=True)
    def __str__(self):
        return self.name    
    class Meta:
        verbose_name_plural = "设备"   

class Staff(models.Model):
    name = models.CharField('员工',max_length=10, unique=True)
    def __str__(self):
        return self.name    
    class Meta:
        verbose_name_plural = "员工"           

class Weixiu(models.Model):
    pline = models.CharField('线别',max_length=1,choices=Pline_choices)
    equi = models.ForeignKey(Equi,on_delete=models.CASCADE,verbose_name='设备')
    date_s = models.DateField('发生日期')
    description = models.TextField('故障/异常/保养维护描述',max_length=200) 
    reason = models.CharField('发生原因',max_length=4,choices=Equi_choices,null=True)
    method = models.TextField('排除方法',max_length=200,null=True) 
    date_e = models.DateField('解决时间',null=True)
    date_n = models.DateField('下次计划维修时间',null=True)
    staff = models.ForeignKey(Staff,on_delete=models.CASCADE,verbose_name='员工',null=True)
    cost = models.DecimalField('费用', max_digits=11, decimal_places=2,null=True,blank=True)
    finish = models.BooleanField('是否完成')
    class Meta:
        verbose_name_plural = "维修单" 
    
class Output(models.Model):
    weixiu = models.ForeignKey(Weixiu,on_delete=models.CASCADE,verbose_name='维修单')
    part  = models.ForeignKey(Parts,on_delete=models.CASCADE,verbose_name='配件编号')
    out_num = models.IntegerField('数量')
    class Meta:
        verbose_name_plural = "出库单" 