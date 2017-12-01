from django.shortcuts import render

# Create your views here.
from pline.models import  JiBen,GuZhang,Yao,JianYu,JianTime

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_jb = JiBen.objects.all().count()
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        #'pline/jbfilter.html',
        context={'num_jb':num_jb},
    )
    
    
from django.views import generic
class JibenListView(generic.ListView):
    model = JiBen   
    template_name = 'pline/jiben_list.html'
    paginate_by = 20
    
# class JibenDetailView(generic.DetailView):
    # model = 基本信息    
    # template_name = 'pline/jiben_detail.html'    
    
from django.shortcuts import get_object_or_404    
from django.db.models import  Sum
def jiben_detail(request, pk):    
    jiben = get_object_or_404(JiBen, pk = pk) 
    gz_count = jiben.guzhang_set.aggregate(Sum('shu')) 
    yao_count = jiben.yao_set.aggregate(Sum('clmj'), Sum('clsl'),Sum('clts')) 
    #如果故障中没有数据，初始化0
    if gz_count['shu__sum'] is None:
        gz_count = {'shu__sum': 0}
    # if yao_count['clmj__sum'] is None:
        # yao_count = {'clmj__sum': 0}
        # yao_count = {'clsl__sum': 0}
        # yao_count = {'clts__sum': 0}    
    
    num =  gz_count['shu__sum'] + jiben.ddw + jiben.cfw + jiben.dqw + jiben.wcw + jiben.qtw
    
    return render(
        request, 
        'pline/jiben_detail.html',
        {'jiben': jiben,'gz_count':gz_count, 'num':num ,'yao_count':yao_count},
    )        

def Jbfilter(request, pl):
    jiben = JiBen.objects.filter(pline = pl)[:30] 
    return render(
        request, 
        'pline/jiben_list.html',
        {'jiben_list': jiben},
    )        
    
def Ljmj(request):
    yao = {}
    pg3441A = Yao.objects.filter(yao=1).filter(jiben__pline  =2).order_by('-jiben__date')[:1]
    yao['pg3441A'] = round(pg3441A[0].ljmj/10000)
    pg3444CS = Yao.objects.filter(yao=2).filter(jiben__pline  =2).order_by('-jiben__date')[:1]
    yao['pg3444CS'] = round(pg3444CS[0].ljmj   /10000)

    pd3124 = Yao.objects.filter(yao=4).filter(jiben__pline=3).order_by('-jiben__date')[:1]
    yao['pd3124'] = round(pd3124[0].ljmj/10000)
    pd3444S = Yao.objects.filter(yao=5).filter(jiben__pline=3).order_by('-jiben__date')[:1]
    yao['pd3444S'] = round(pd3444S[0].ljmj/10000)
    pd3447S = Yao.objects.filter(yao=6).filter(jiben__pline=3).order_by('-jiben__date')[:1]
    yao['pd3447S'] = round(pd3447S[0].ljmj/10000)
    
    pg2441A = Yao.objects.filter(yao=1).filter(jiben__pline=1).order_by('-jiben__date')[:1]
    yao['pg2441A'] = round(pg2441A[0].ljmj/10000)
    pg2444CS = Yao.objects.filter(yao=2).filter(jiben__pline=1).order_by('-jiben__date')[:1]
    yao['pg2444CS'] = round(pg2444CS[0].ljmj/10000)
    pg2447MD = Yao.objects.filter(yao=3).filter(jiben__pline=1).order_by('-jiben__date')[:1]
    yao['pg2447MD'] = round(pg2447MD[0].ljmj/10000)    
    
    return render(
        request,
        'pline/ljmj.html',
        {'yao':yao},
    )
    
def Buliang(request):
    buliang = []
    #选择200条记录，差不多3个月的记录
    bl = JiBen.objects.filter(date__year__gte=2017)[:200] 
    for bu in bl:
        if bu.sum_bl() > 0 :
            buliang.append(bu)
    return render(
        request,
        'pline/buliang.html',
        {'bl':buliang},
    )
    
def Jianyu(request):
    jy = []
    jianyu = JianYu.objects.all()
    for jian in jianyu:
        bu = {}
        bu['name'] = jian.name
        bu['mianji'] = jian.mianji
        jiantime = JianTime.objects.filter(jianyu_id = jian.id).order_by('-date')
        if jiantime :
            bu['date'] = jiantime[0].date            
        if jian.name.find('PG2') >= 0:
            pline = '1'
        if jian.name.find('PG3') >= 0:
            pline = '2'   
        if jian.name.find('PD3') >= 0:
            pline = '3'                  
        clmj = JiBen.objects.filter(pline=pline).filter(date__gte=bu['date']).aggregate(mj = Sum('clmj')) 
        if clmj['mj']:
            bu['clmj'] = round(clmj['mj'] / 10000)
        else:
            bu['clmj'] = 0
        jy.append(bu) 
    return render(
        request,
        'pline/jianyu.html',
        {'jy':jy},
   )