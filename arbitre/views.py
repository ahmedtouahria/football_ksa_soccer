""" ==== Arbitre LOGIC === """
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions,status
from account.permissions import *
from arbitre.serializers import *
from club.models import *
from .models import *
from rest_framework import generics,viewsets
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from knox.auth import TokenAuthentication
from django.utils.translation import gettext_lazy as _
from rest_framework.decorators import api_view,action

from account.functions import try_except_model
""" view matchs not geted arbiter in home page """
class ListMatchs(generics.ListCreateAPIView):
    queryset =Match.objects.filter(arbitre=None,finished=False)
    serializer_class = HomeMatchsSerializer
    authentication_classes=[TokenAuthentication]
    def post(self, request, *args, **kwargs):
        return Response({"method not allowed !"})


class SendOrderMatch(generics.ListCreateAPIView):
    serializer_class = SendMatchOrderSerializer
    #permission_classes = [IsArbitre,]
    # order arbitre list 
    def list(self, request, *args, **kwargs):
        self_arbitre = try_except_model(model=Arbitre,to=request.user,type="user")
        if self_arbitre:
            queryset = OrderArbitreMatch.objects.filter(arbitre=self_arbitre)
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response({"message":"fack you you are not arbitre"},status=status.HTTP_401_UNAUTHORIZED)
    def create(self, request, *args, **kwargs):
        if request.user.arbitre:
            serializer = self.get_serializer(data=request.data)
            id_match = request.data.get("match",None)
            self_match = try_except_model(Match,id_match,"id")
            self_arbitre = try_except_model(Arbitre,request.user,"user")
            if OrderArbitreMatch.objects.filter(arbitre=self_arbitre,match=self_match).exists():
                return Response({_('object already existed !')},status=status.HTTP_406_NOT_ACCEPTABLE)
            serializer.is_valid(raise_exception=True)
            OrderArbitreMatch.objects.create(arbitre=self_arbitre,match=self_match,price=request.data.get("price"))
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            Response("not allowed (you are not authenticated or not arbitre)",status=status.HTTP_401_UNAUTHORIZED)

class ListMatchsReserver(viewsets.ModelViewSet):
    serializer_class = HomeMatchsSerializer
    permission_classes = [IsArbitreOnly]
    def get_queryset(self):
        try:
            self_arbitre=Arbitre.objects.get(user=self.request.user)
        except:
            self_arbitre=None
        if self_arbitre:
            queryset = Match.objects.filter(arbitre=self_arbitre,finished=False)
        else:
            queryset=[]
        return queryset
    @action(detail=True, methods=['post','put'],permission_classes=[IsArbitreOnly,])
    def set_player_card(self, request, pk=None):
        serializer = SendMatchCardSerializer(data=request.data)
        if serializer.is_valid():
            this_match=try_except_model(Match,pk,"id")
            player=try_except_model(Player,request.data.get("player"),"id")
            if this_match.arbitre.user == request.user:
                if this_match:
                    if MatchCard.objects.filter(match=this_match,card=request.data.get('card'),player=player).exists():
                        return Response("object exsisted",status=status.HTTP_406_NOT_ACCEPTABLE)
                    serializer.save(match=this_match)
                    return Response({'status': f'card {request.data.get("card")} set to this user'},status=status.HTTP_201_CREATED)
                else:
                    return Response({"Match is None"},status=status.HTTP_404_NOT_FOUND)
            else:
                return Response(_("you are not a self arbitre !"),status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
    @action(detail=True, methods=['post','put'],permission_classes=[IsArbitreOnly,])
    def set_player_goal(self, request, pk=None):
        serializer = SendPLayerGoalSerializer(data=request.data)
        if serializer.is_valid():
            this_match=try_except_model(Match,pk,"id")
            player=try_except_model(Player,request.data.get("player"),"id")
            if this_match.arbitre.user == request.user:
                if this_match:
                    penalty=request.data.get('is_penalty',False)
                    sel_request = GoalMatch.objects.filter(match=this_match,player=player)
                    if sel_request:
                        sel_request.update(is_penalty=penalty)
                        return Response("object exsisted",status=status.HTTP_406_NOT_ACCEPTABLE)
                    serializer.save(match=this_match)
                    return Response({'status': f'goal set to this user'},status=status.HTTP_201_CREATED)
                else:
                    return Response({"Match is None"},status=status.HTTP_404_NOT_FOUND)
            else:
                return Response(_("you are not a self arbitre !"),status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
     
    def create(self, request, *args, **kwargs):
        return Response({"method not allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    def destroy(self, request, *args, **kwargs):
        return Response({"method not allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    def update(self, request, *args, **kwargs):
        if request.method == "PATCH":
            if ("score_one" or "score_two" in request.data) and len(request.data)<=2:
                partial = kwargs.pop('partial', False)
                instance = self.get_object()
                serializer = self.get_serializer(instance, data=request.data, partial=partial)
                serializer.is_valid(raise_exception=True)
                self.perform_update(serializer)
                if getattr(instance, '_prefetched_objects_cache', None):
                    # If 'prefetch_related' has been applied to a queryset, we need to
                    # forcibly invalidate the prefetch cache on the instance.
                    instance._prefetched_objects_cache = {}
                return Response(serializer.data)
            else:
                return Response({"you dont have this permission"},status=status.HTTP_401_UNAUTHORIZED)
        else: return Response({"method not allowed"},status=status.HTTP_401_UNAUTHORIZED)