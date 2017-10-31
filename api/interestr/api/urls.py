from django.conf.urls import url
from django.contrib import admin

from . import views
from rest_framework.authtoken import views as rf_views
from rest_framework.documentation import include_docs_urls

app_name='api'
urlpatterns = [
    url(r'^docs/', include_docs_urls(title='Interestr API')),

    url(r'^login/$', rf_views.obtain_auth_token, name='token_auth'),
    url(r'^users/$', views.UserList.as_view(), name='users'),
    url(r'^users/(?P<pk>\d+)/$', views.UserDetail.as_view(), name='userdetail'),
    url(r'^posts/$', views.PostList.as_view(), name='posts'),
    url(r'^posts/(?P<pk>\d+)/$', views.PostDetail.as_view(), name='postdetail'),
    url(r'^data_templates/$', views.DataTemplateList.as_view(), name='datatemplates'),
    url(r'^data_templates/(?P<pk>\d+)/$', views.DataTemplateDetail.as_view(), name='datatemplatedetail'),
    url(r'^groups/$', views.GroupList.as_view(), name='groups'),
    url(r'^groups/(?P<pk>\d+)/$', views.GroupDetail.as_view(), name='groupDetail'),

    url(r'^users/groups/(?P<pk>\d+)/$', views.memberGroupOperation),
]
