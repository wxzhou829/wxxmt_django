from django.db import models

from django.urls import reverse #Used to generate URLs by reversing the URL patterns
# Create your models here.


pline_choices = (
    ('1','PG2'),
    ('2','PG3'),
    ('3','PD3'),
)
   

#定义基本信息表jiben
class JiBen(models.Model):
    pline = models.CharField('线别',max_length=1,choices=pline_choices)
    date =  models.DateField('日期')
    kjcs = models.IntegerField('开机次数', default=0) 
    clmj = models.IntegerField('处理面积', default=0)  
    trl = models.IntegerField('投入量', default=0) 
    scss = models.IntegerField('生产时数', default=0) 
    yygs = models.IntegerField('应有杆数', default=0)
    bl  = models.IntegerField('不良数', default=0)
    amp  = models.IntegerField('安培小时', default=0)
    shui = models.IntegerField('用水量', default=0)
    dian = models.IntegerField('用电量', default=0)
    
    #未稼动数据
    ddw = models.IntegerField('品质等待', default=0)      
    cfw = models.IntegerField('换班吃饭',default=0)   
    dqw = models.IntegerField('货源短缺',default=0)       
    wcw = models.IntegerField('开关机误差',default=0)   
    qtw = models.IntegerField('其他',default=0)  
    
    #不良数据
    sc_choices = (
    ('c','操作不当'),
    ('y','药液失调'),
    ('g','故障设备'),
    )
    mh_choices = (
    ('c','操作不当'),
    ('j','计算错误'),
    ('g','故障设备'),
    )
    cs_choices = (
    ('c','操作不当'),
    ('p','票据错误'),
    ('g','故障设备'),
    )
    qp_choices = (
    ('m','膜厚偏高'),
    ('s','酸洗不良'),
    ('g','故障设备'),
    )
    ct_choices = (
    ('d','导电不良'),
    ('f','挂具不符'),
    ('t','脱脂不良'),
    ('g','故障设备'),
    )
    qt_choices = (
    ('j','基材不良'),
    ('h','素材黑点'),
    ('s','素材生锈'),
    )
    
    sc_count = models.IntegerField('色差数量', default=0)  
    scy = models.CharField('色差原因',max_length=1,choices=sc_choices,null=True) 
    mh_count = models.IntegerField('膜厚数量', default=0)  
    mhy = models.CharField('膜厚原因',max_length=1,choices=mh_choices,null=True) 
    cs_count = models.IntegerField('错色数量', default=0)  
    csy = models.CharField('错色原因',max_length=1,choices=cs_choices,null=True) 
    qp_count = models.IntegerField('气泡数量', default=0)  
    qpy = models.CharField('气泡原因',max_length=1,choices=qp_choices,null=True) 
    ct_count = models.IntegerField('出铁数量', default=0)  
    cty = models.CharField('出铁原因',max_length=1,choices=ct_choices,null=True)
    qt_count = models.IntegerField('其他数量', default=0)  
    qty = models.CharField('其他原因',max_length=1,choices=qt_choices,null=True)  
    
    # Metadata
    class Meta: 
        ordering = ["-date",'pline']
        verbose_name_plural = "基本信息表"
        
    def sum_bl(self):
        return self.sc_count + self.mh_count + self.cs_count + self.qp_count + self.ct_count + self.qt_count          
        
    def get_absolute_url(self):
        return reverse('jiben-detail', args=[str(self.id)])
    
#定义故障表guzhang
class GuZhang(models.Model):
    name = models.CharField('故障原因',max_length=50) 
    shu = models.IntegerField('故障数量', default=0)
    f_date = models.DateTimeField('发生时间')
    x_date = models.DateTimeField('修复时间')
    jiben = models.ForeignKey(JiBen, on_delete=models.CASCADE)
    banci_choices = (
    ('A','A班'),
    ('B','B班'),
    )
    banci = models.CharField(
        max_length=1,
        choices=banci_choices,
    )
    
    # Metadata
    class Meta: 
        verbose_name_plural = "故障"    

yao_choices = (
    ('1','441A'),
    ('2','444CS'),
    ('3','447MD'),
    ('4','124'),
    ('5','444S'),  
    ('6','447S'),  
)        
        
#定义药水处理表yaocl
class Yao(models.Model):
    yao = models.CharField('药水',max_length=1,choices=yao_choices)  
    jiben = models.ForeignKey(JiBen, on_delete=models.CASCADE)
    clmj = models.IntegerField('处理面积', default=0)  
    clsl = models.IntegerField('处理数量', default=0) 
    clts = models.IntegerField('处理桶（杆）数', default=0) 
    ljmj = models.IntegerField('累积面积', default=0) 
    class Meta: 
        verbose_name_plural = "药水" 

#PD3加药表    
class JiaPD3(models.Model):
    date = models.DateField('日期')
    ct = models.IntegerField('初脱', default=0)  
    cd = models.IntegerField('初电', default=0)  
    cdpj = models.IntegerField('初电片碱', default=0)  
    dj = models.IntegerField('电解', default=0)  
    djpj = models.IntegerField('电解片碱', default=0)  
    ys = models.IntegerField('盐酸', default=0)  
    xb = models.IntegerField('锌板', default=0)  
    lj = models.IntegerField('粒碱', default=0)  
    nz98 = models.IntegerField('NZ-98', default=0)  
    nzfb = models.IntegerField('NZ-FB', default=0)  
    h0616y = models.IntegerField('H-0616Y', default=0)  
    hztzj = models.IntegerField('HZ调整剂', default=0)  
    j124 = models.IntegerField('124', default=0)  
    j44s = models.IntegerField('44S', default=0)  
    j44h = models.IntegerField('44H', default=0)  
    j447s1 = models.IntegerField('447S1', default=0)   
    j447s2 = models.IntegerField('447S2', default=0)  
    j447s3 = models.IntegerField('447S3', default=0)  
    j447r3 = models.IntegerField('447R3', default=0)  
    j118n = models.IntegerField('118N', default=0)  
    
    # Metadata
    class Meta: 
        ordering = ["-date"]
        verbose_name_plural = "PD3加药表"

#PG2加药表          
class JiaPG2(models.Model):
    date = models.DateField('日期')                              
    sc30 = models.IntegerField('SC-30', default=0)                
    hcl = models.IntegerField('HCL', default=0)                 
    rc30 = models.IntegerField('RC-30', default=0)            
    rc25st = models.IntegerField('RC-25ST', default=0)              
    ds31 = models.IntegerField('DS-31', default=0)            
    naoh = models.IntegerField('NAOH', default=0)                
    xb = models.IntegerField('锌板', default=0)                  
    lj = models.IntegerField('粒碱', default=0)                  
    nz200r = models.IntegerField('NZ-200R', default=0)             
    nzrba = models.IntegerField('NZ-RBA', default=0)              
    h0616y = models.IntegerField('H-0616Y', default=0)           
    hztzj = models.IntegerField('HZ调整剂', default=0)           
    j441a = models.IntegerField('441A', default=0)          
    j444cs = models.IntegerField('444CS', default=0)         
    j444cst = models.IntegerField('444CST', default=0)        
    j447md1 = models.IntegerField('447MD1', default=0)      
    j447md2 = models.IntegerField('447MD2', default=0)      
    j447md3 = models.IntegerField('447MD3', default=0)      
    j447md4 = models.IntegerField('447MD4', default=0)      
    j447md7 = models.IntegerField('447MD7', default=0) 
    j118 = models.IntegerField('ZTB-118', default=0)    
                                                                 
    # Metadata
    class Meta: 
        ordering = ["-date"]
        verbose_name_plural = "PG2加药表"  
        
#PG3加药表       
class JiaPG3(models.Model):
    date = models.DateField('日期')                           
    sc30 = models.IntegerField('SC-30', default=0)            
    hcl = models.IntegerField('HCL', default=0)               
    rc30 = models.IntegerField('RC-30', default=0)            
    rc25st = models.IntegerField('RC-25ST', default=0)         
    sm = models.IntegerField('DS-31', default=0)              
    naoh = models.IntegerField('NAOH', default=0)             
    xb = models.IntegerField('锌板', default=0)               
    lj = models.IntegerField('粒碱', default=0)               
    nz200r = models.IntegerField('NZ-200R', default=0)        
    nzrba = models.IntegerField('NZ-RBA', default=0)          
    h0616y = models.IntegerField('H-0616Y', default=0)        
    hztzj = models.IntegerField('HZ调整剂', default=0)        
    j441a = models.IntegerField('441A', default=0)            
    j444cs = models.IntegerField('444CS', default=0)          
    j444cst = models.IntegerField('444CST', default=0)        
  
                                                                 
    # Metadata
    class Meta: 
        ordering = ["-date"]
        verbose_name_plural = "PG3加药表"      

#     其他费用表   
class Cost(models.Model):
    o_date = models.DateField('日期')                           
    jbss = models.IntegerField('加班时数', default=0)  
    jbxs = models.IntegerField('加班系数', default=0)  
    sbyl = models.IntegerField('水表用量', default=0)  
    sdj = models.IntegerField('水单价', default=6)  
    wsf = models.IntegerField('污水费', default=57)  
    qbyl = models.IntegerField('汽表用量', default=0)  
    qdj = models.IntegerField('汽单价', default=408)  
    lbf = models.IntegerField('挂具维修费', default=0)  
    bzf = models.IntegerField('包装费', default=0) 
    bgf = models.IntegerField('修理费', default=0) 
    dzyh = models.IntegerField('低值易耗', default=0)
    wlxh = models.IntegerField('物料消耗', default=0)
    other = models.IntegerField('原料（药品）', default=0)   
    # Metadata
    class Meta: 
        ordering = ["-o_date"]
        verbose_name_plural = "其他费用表"   

# 其他费用表(月)       
from datetime import date        
class CostMonth(models.Model):
    mo = date.today()
    o_date = models.CharField('日期', max_length=6, default = mo.strftime("%Y%m") ,help_text='请输入年份和月份')                           
    jbf = models.IntegerField('加班费', default=0)              
    sf = models.IntegerField('水费', default=0)              
    zqf = models.IntegerField('蒸汽费', default=0)             
    lbf = models.IntegerField('劳保费', default=0)            
    bgf = models.IntegerField('办公费', default=0)             
    dzyh = models.IntegerField('低值易耗', default=0)        
    wlxh = models.IntegerField('物料消耗', default=0)          
    other = models.IntegerField('原料（药品）', default=0) 
    bzf = models.IntegerField('包装费', default=0)     
    # Metadata
    class Meta: 
        ordering = ["-o_date"]
        verbose_name_plural = "其他费用表(月)"  
        
#累积面积设定表
class MaxMJ(models.Model):
    pline = models.CharField('线别',max_length=1,choices=pline_choices,default='1')
    yao = models.CharField('药水',max_length=1,choices=yao_choices)   
    maxV =  models.IntegerField('最大值(万)', default=0) 
    
    class Meta:
        verbose_name_plural = "累积面积最大值设定"  
        
        
#全检 客户 名称
class Quanjian(models.Model):
    customer = models.CharField('客户',max_length=50)
    jianming = models.CharField('件名',max_length=50)   
    jianhao =  models.CharField('件号',max_length=50) 
    
    class Meta:
        verbose_name_plural = "全检名称设定"    
    def __str__(self):
        return self.jianhao       
        
#全检数据表
class Quandata(models.Model):
    date = models.DateField('日期')
    quanjian = models.ForeignKey(Quanjian, on_delete=models.CASCADE,verbose_name='全检件号')
    total = models.IntegerField('总量', default=0) 
    baofeng = models.IntegerField('包风/出铁', default=0) 
    yaoshuiheng = models.IntegerField('药水痕', default=0) 
    shuiyin = models.IntegerField('水印/水渍', default=0) 
    fengbicanliu = models.IntegerField('封闭残留', default=0)  
    fahei = models.IntegerField('发黑', default=0) 
    fahuang = models.IntegerField('发黄', default=0) 
    fawu = models.IntegerField('发雾', default=0) 
    zangwu = models.IntegerField('脏污', default=0) 
    guashang = models.IntegerField('刮伤', default=0) 
    fancai = models.IntegerField('泛彩', default=0) 
    qipao = models.IntegerField('气泡', default=0) 
    seze = models.IntegerField('色泽/色差', default=0) 
    bianxing = models.IntegerField('变形', default=0) 
    cuose = models.IntegerField('错色', default=0) 
    dianzuoshang = models.IntegerField('电灼伤', default=0) 
    xiushi = models.IntegerField('锈蚀', default=0) 

    class Meta:
        verbose_name_plural = "全检数据"   
        ordering = ["-date"]
        
#水表
class Water(models.Model):   
    date = models.DateField('日期')
    pg3 = models.IntegerField('滚一线', default=0) 
    pg2a = models.IntegerField('滚二线A', default=0) 
    pg2c = models.IntegerField('滚二线C', default=0) 
    pg2d = models.IntegerField('滚二线D', default=0) 
    pd3 = models.IntegerField('吊镀线', default=0) 
    plat_5m = models.IntegerField('五米平台', default=0) 
    f_toilet = models.IntegerField('前面厕所', default=0) 
    b_toilet = models.IntegerField('后面厕所', default=0) 
    b_roof = models.IntegerField('后楼顶', default=0) 
    lab = models.IntegerField('实验室', default=0) 
    final_water = models.IntegerField('终水', default=0) 
    pure_water = models.IntegerField('纯水', default=0) 
    main_water = models.IntegerField('总表（外）', default=0) 
    main_water_n = models.IntegerField('总表（内）', default=0) 
    
    class Meta:
        verbose_name_plural = "水表"   
        ordering = ["-date"]

#建浴面积设定
class JianYu(models.Model):
    name = models.CharField('槽名', max_length=30)
    mianji = models.IntegerField('建浴面积（万）')
    class Meta:
        verbose_name_plural = '建浴面积'
    def __str__(self):
        return self.name     
    
#建浴时间
class JianTime(models.Model):
    jianyu = models.ForeignKey(JianYu,on_delete=models.CASCADE)
    date = models.DateField('日期')
    class Meta:
        verbose_name_plural = '建浴'