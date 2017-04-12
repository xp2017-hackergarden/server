from django.conf.urls import url
from xpserver_web import views


# patterns here are prefixed with 'web/'
urlpatterns = [
    url(r'^ping$', views.ping),
    url(r'^$', views.hello_world)
]
