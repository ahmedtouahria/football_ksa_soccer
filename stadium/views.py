""" ==== Arbitre LOGIC === """
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.response import Response
from rest_framework import authentication, permissions,status
from stadium.permissions import *
from stadium.serializers import *
from club.models import *
from .models import *
from rest_framework import generics,viewsets
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from knox.auth import TokenAuthentication
from django.utils.translation import gettext_lazy as _
from rest_framework.decorators import api_view,action

class ListMyStadium(viewsets.ModelViewSet):
    serializer_class = StadiumSerializer
    permission_classes = [IsStadiumOwnerOrReadOnly]
    def get_queryset(self):
        queryset = Stadium.objects.filter(owner__user=self.request.user)
        return queryset

class MyOrdersStadiums(viewsets.ModelViewSet):
    serializer_class = StadiumOrderSerializer
    permission_classes = [IsStadiumOwnerOrReadOnlyForOrders]
    def get_queryset(self):
        try:
            queryset = OrderStadium.objects.filter(stadium__owner__user=self.request.user)
        except :
            queryset=[]
        return queryset
    def create(self, request, *args, **kwargs):
        return Response({"method not allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    def delete(self, request, *args, **kwargs):
        return Response({"method not allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    def update(self, request, *args, **kwargs):
        print(len(request.data))
        if (request.method=="PATCH") and ('status' in request.data) and (len(request.data)==1):
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            if getattr(instance, '_prefetched_objects_cache', None):
                instance._prefetched_objects_cache = {}
            return Response(serializer.data)
        return Response({"method not allowed you can update status only"}, status=status.HTTP_401_UNAUTHORIZED)
