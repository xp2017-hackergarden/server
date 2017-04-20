from xpserver_api import views
from django.conf.urls import url, include
from rest_framework import routers
from xpserver_api.serializers import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^activate_account/$', views.activate_account, name='activate')

]
