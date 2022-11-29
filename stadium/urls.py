from django.urls import path,include
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'stadiums', ListMyStadium, basename='stadiums')
router.register(r'orders', MyOrdersStadiums, basename='orders')

urlpatterns = [ 
    path('',include(router.urls)), 
]
