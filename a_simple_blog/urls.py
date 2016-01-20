from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<id>[0-9]+)/$', views.edit, name='edit'),
    url(r'^add$', views.add, name='add'),
    url(r'^delete_post/(?P<id>[0-9]+)/$', views.delete_post, name='delete_post'),

]