from django.conf.urls import url
from xpserver_web import views

# patterns here are prefixed with '/'
urlpatterns = [
    url(r'^ping$', views.ping),
    url(r'^$', views.main, name='home'),
    url(r'^register/$', views.register, name='register'),
    url(r'^change-password/$', views.change_password, name='change_password'),
]
