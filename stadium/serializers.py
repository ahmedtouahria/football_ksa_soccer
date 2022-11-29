from rest_framework import serializers
from account.models import User
from club.models import *
from .models import *
from rest_framework.validators import UniqueTogetherValidator
from rest_framework.response import Response

class StadiumSerializer(serializers.ModelSerializer):
    #owner = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Stadium
        fields = ['name','owner','localisation','price','promo_price','image']
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "phone","state","image"]
class CreatedBySerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class  Meta:
        model = Capitan
        fields=['user',]

class StadiumOrderSerializer(serializers.ModelSerializer):
    #owner = serializers.PrimaryKeyRelatedField(read_only=True)
    stadium = StadiumSerializer()
    created_by=CreatedBySerializer()
    class Meta:
        model = OrderStadium
        fields = ['match','created_by','status','stadium']