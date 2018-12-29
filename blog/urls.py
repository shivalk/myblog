from django.conf.urls import url
from django.urls import include,path,re_path
from . import views

app_name='blog'

urlpatterns = [
    #url(r'$^',views.post_list,name='post_list'),
    url(r'^$',views.PostListView.as_view(),name='post_list'),
    url(r'^$', views.PostListView.as_view(), name='post_list'),

    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'r'(?P<post>[-\w]+)/$',views.post_detail,name='post_detail'),
    # re_path(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'r'(?P<post>[-\w]+)/$',views.post_detail,name='post_detail'),
    
    url(r'^(?P<post_id>\d+)/share/$',views.post_share,name='post_share')
]
