from django.conf.urls import url
from .views import post_list, post_detail, new_post
from . import views

urlpatterns = [
    url(r'^$', post_list),
    url(r'^(?P<id>\d+)/$', post_detail),
    url(r'^post/new/$', new_post, name='new_post'),
]