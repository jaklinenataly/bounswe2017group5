from django.conf.urls import url
from django.contrib import admin

from . import views
from rest_framework.authtoken import views as rf_views

app_name = 'api'
urlpatterns = [
    url(r'^login/$', rf_views.obtain_auth_token, name='token_auth'),
    url(r'^register/$', views.SignUpView.as_view(), name='register'),

    url(r'^users/$', views.UserList.as_view(), name='users'),
    url(r'^users/(?P<pk>\d+)/$', views.UserDetail.as_view(), name='userdetail'),

    url(r'^posts/$', views.PostList.as_view(), name='posts'),
    url(r'^posts/(?P<pk>\d+)/$', views.PostDetail.as_view(), name='postdetail'),

    url(r'^tags/$', views.TagList.as_view(), name='tags'),
    url(r'^tags/(?P<pk>\d+)/$', views.TagDetail.as_view(), name='tagdetail'),

    url(r'^comments/$', views.CommentList.as_view(), name='comments'),
    url(r'^comments/(?P<pk>\d+)/$',
        views.CommentDetail.as_view(), name='commentdetail'),
    url(r'^votes/$', views.VoteList.as_view(), name='votes'),
    url(r'^votes/(?P<pk>\d+)/$', views.VoteDetail.as_view(), name='votedetail'),
    url(r'^files/$', views.FileList.as_view(), name='files'),
    url(r'^files/(?P<pk>\d+)/$', views.FileDetail.as_view(), name='filedetail'),

    url(r'^profile_pages/$', views.ProfilePageList.as_view(), name='profilepages'),
    url(r'^profile_pages/(?P<pk>\d+)/$',
        views.ProfilePageDetail.as_view(), name='profilepagedetail'),

    url(r'^annotations/$', views.AnnotationList.as_view(), name='annotations'),
    url(r'^annotations/(?P<pk>\d+)/$',
        views.AnnotationDetail.as_view(), name='annotationdetail'),

    url(r'^data_templates/$', views.DataTemplateList.as_view(), name='datatemplates'),
    url(r'^data_templates/(?P<pk>\d+)/$',
        views.DataTemplateDetail.as_view(), name='datatemplatedetail'),

    url(r'^groups/$', views.GroupList.as_view(), name='groups'),
    url(r'^groups/(?P<pk>\d+)/$', views.GroupDetail.as_view(), name='groupdetail'),
    url(r'^me/$', views.CurrentUserView.as_view(), name='currentuser'),
    url(r'^follow/profile/(?P<pk>\d+)/$',
        views.FollowOperation.as_view(), name='followoperation'),
    url(r'^users/groups/(?P<pk>\d+)/$',
        views.MemberGroupOperation.as_view(), name='groupoperation'),
    url(r'^search_wiki/$', views.search_wikidata, name="searchwiki"),
    url(r'^recommend_groups/$', views.recommend_groups, name='recommendgroups'),
    url(r'^recommend_posts/$', views.recommend_posts, name='recommendposts'),
    url(r'^template_search/$', views.search_posts_by_template, name='templatesearch'),

]
