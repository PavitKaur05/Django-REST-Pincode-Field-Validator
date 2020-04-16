from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views
router=DefaultRouter()
router.register('pincode',views.PinCodeViewSet,basename='pincode')
urlpatterns=[path('',include(router.urls))]
