from django.conf.urls import url
from django.views.generic import TemplateView
from .views import PublisherList, PostCreate, PostUpdate, PostDelete

from . import views


urlpatterns = [
    url(r'^$', PublisherList.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/edit/$', PostUpdate.as_view(), name='edit'),
    url(r'^add/$', PostCreate.as_view(), name='add'),
    url(r'^(?P<pk>[0-9]+)/delete_post/$', PostDelete.as_view(), name='delete_post'),

]