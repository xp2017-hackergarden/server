from django.conf.urls import url
from xpserver_api import views

urlpatterns = [
    url(r'^activate_account/$', views.activate_account, name='activate')
]
