""" ==== Arbitre LOGIC === """
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.response import Response
from rest_framework import authentication, permissions,status
from .permissions import *
from .serializers import *
from club.models import *
from .models import *
from rest_framework import generics,viewsets
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from knox.auth import TokenAuthentication
from django.utils.translation import gettext_lazy as _
from rest_framework.decorators import api_view,action




class ClubeViewSet(viewsets.ModelViewSet):
    """ 
    Create Clube an get -> /api/clube/create_clube/
    """
    serializer_class = ClubeSerializer
    permission_classes = [IsClubeCapitanOrReadOnly]
    queryset= Clube.objects.all()


""" My Clube Memeber 'crud actions' /api/clube/my_clube_members/  """

"""Invite player to join my club /api/clube/invite_player/ """

"""players orders to join my club accepte or rejecte or wait /api/clube/players_orders/"""

"""create match with other clube /api/clube/create_match/"""

