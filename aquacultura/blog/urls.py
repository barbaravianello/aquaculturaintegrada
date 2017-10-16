from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='home'),
    url(r'^post/(?P<slug>[\w_-]+)/$', views.post_detail, name='post_detail'),
    url(r'^categoria/(?P<slug>[\w_-]+)/$', views.category_posts, name='category_posts'),
    url(r'^search/$', views.search, name='search'),
    url(r'^search/(?P<q>[\w_-]+)/$', views.search, name='search'),
]
