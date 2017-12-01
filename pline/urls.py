from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^jiben/$', views.JibenListView.as_view(), name='jiben'),
    url(r'^ljmj/$', views.Ljmj, name='ljmj'),
    url(r'^bl/$', views.Buliang, name='buliang'),
    url(r'^jy/$', views.Jianyu, name='jianyu'),
    url(r'^jb/(?P<pl>\d+)$', views.Jbfilter, name='jbfilter'),
    url(r'^jiben/(?P<pk>\d+)$', views.jiben_detail, name='jiben-detail'),
]
