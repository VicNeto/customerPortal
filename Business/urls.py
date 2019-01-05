#Business Urls configuration

#Django
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf.urls import url
from CustomerData import views

#Routers
router = routers.DefaultRouter()
router.register('v1/portal/customer', views.UserViewSet)

urlpatterns = [
    path('',include('CustomerData.urls')),
    path('customer/', include('CustomerData.urls')),
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
