from django.urls import path,include
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'clubes', ClubeViewSet, basename='matchs_reserved')

urlpatterns = [ 
    path('',include(router.urls)), 
]

