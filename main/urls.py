from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^get_data/$', views.chart_build, name='cart_build'),
    url(r'^get_data/(?P<group_id>\d+)/$', views.chart_build, name='chart_build'),
]