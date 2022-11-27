from django.urls import path,include
from .views import *
from rest_framework import routers
from knox.views import LogoutView


router = routers.DefaultRouter()
router.register(r'matchs_reserved', ListMatchsReserver, basename='matchs_reserved')

urlpatterns = [ 
    path('',include(router.urls)), 
    path("matchs/",ListMatchs.as_view()),
    path("send_match_order/",SendOrderMatch.as_view()),
]

