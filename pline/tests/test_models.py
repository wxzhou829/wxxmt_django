from django.test import TestCase

# Create your tests here.
from pline.models import  JiBen,GuZhang,Yao
from django.utils import timezone

class jbModelTest(TestCase):
    def setUp(self):
        #创建基本信息
        test_jb = JiBen.objects.create(
        pline='PD3', date='2017-11-10', kjcs = 0, clmj = 138059, trl = 220169, scss =24 ,
        yygs = 1440, amp  = 46029, bl = 0, shui =34, dian = 0,
        ddw = 2, cfw = 3 , dqw = 4, wcw = 5, qtw =6,
        sc_count = 21, mh_count =22, cs_count =23, qp_count =24, ct_count =25, qt_count =26,
        )
    
    def test_pline_label(self):
        jb = 基本信息.objects.get(id=1)
        field_label = jb._meta.get_field('pline').verbose_name
        #print(jb.scy)
        self.assertEquals(field_label,'线别')
        
        max_length = jb._meta.get_field('pline').max_length
        self.assertEquals(max_length,1)    

        #This will also fail if the urlconf is not defined.
        self.assertEquals(jb.get_absolute_url(),'/pline/jiben/1')


class gzModelTest(TestCase):      
    def setUp(self):
        #创建基本信息
        test_jb = 基本信息.objects.create(
        pline='PD2', date='2017-11-10', kjcs = 0, clmj = 138059, trl = 220169, scss =24 ,
        yygs = 1440, amp  = 46029, bl = 0, shui =34, dian = 0,
        ddw = 2, cfw = 3 , dqw = 4, wcw = 5, qtw =6,
        sc_count = 21, mh_count =22, cs_count =23, qp_count =24, ct_count =25, qt_count =26,
        )
        
        #创建2个故障
        test_gz1 = 故障.objects.create(
        name = '天车不动1' , count = 10, f_date = '2017-11-9 06:00:00' ,
        x_date = '2017-11-9 07:00:00' , jiben = test_jb
        )
        
        test_gz2 = 故障.objects.create(
        name = '天车不动2' , count = 20, f_date = '2017-11-9 08:00:00' ,
        x_date = '2017-11-9 09:00:00' , jiben = test_jb
        )        
    
    def test_gz_lable(self):
        gz = 故障.objects.get(id=1)
        field_label = gz._meta.get_field('name').verbose_name   
        #print(gz.f_date)   
        self.assertEquals(field_label,'故障原因')

        
class yaoModelTest(TestCase):      
    def setUp(self):
        #创建基本信息
        test_jb = 基本信息.objects.create(
            pline='PD2', date='2017-11-10', kjcs = 0, clmj = 138059, trl = 220169, scss =24 ,
            yygs = 1440, amp  = 46029, bl = 0, shui =34, dian = 0,
            ddw = 2, cfw = 3 , dqw = 4, wcw = 5, qtw =6,
            sc_count = 21, mh_count =22, cs_count =23, qp_count =24, ct_count =25, qt_count =26,
        )
        
        #创建3个 药水处理
        test_yao1 = 药水处理.objects.create(
            yao = '160' ,  clmj = 123 , clsl =234, clts = 23 ,
            ljmj = 0 , jiben = test_jb
        )
        test_yao2 = 药水处理.objects.create(
            yao = '162' ,  clmj = 2123 , clsl = 2234, clts = 23 ,
            ljmj = 0 , jiben = test_jb
        )        
        test_yao3 = 药水处理.objects.create(
            yao = '173' ,  clmj = 3123 , clsl =3234, clts = 23 ,
            ljmj = 0 , jiben = test_jb
        )        
        

    def test_yao_lable(self):
        yao = 药水处理.objects.get(id=2)
        field_label = yao._meta.get_field('yao').verbose_name   
        #print(yao.clmj)   
        self.assertEquals(field_label,'药水')      
    
    
    


