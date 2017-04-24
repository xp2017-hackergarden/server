from xpserver_api import views
from django.conf.urls import url, include
from rest_framework import routers
from xpserver_api.serializers import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^activate_account/$', views.activate_account, name='activate'),
    url(r'^activate_mobile_app/$', views.activate_mobile_app, name='activate_mobile_app')
]
