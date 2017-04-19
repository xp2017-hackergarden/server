from django.conf.urls import url
from xpserver_web import views

# patterns here are prefixed with '/'
urlpatterns = [
    url(r'^ping$', views.ping),
    url(r'^$', views.main),
    url(r'^register/$', views.register, name='register'),
]
