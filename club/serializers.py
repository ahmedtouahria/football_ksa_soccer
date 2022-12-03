from rest_framework import serializers
from account.models import User
from club.models import *
from stadium.serializers import UserSerializer
from .models import *
from rest_framework.response import Response


class ClubeSerializer(serializers.ModelSerializer):
    capitan = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Clube
        fields = ['id', 'name', 'capitan', 'active', 'logo']
class PlayerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Player
        fields = ['user', 'nickname',]
class ClubePlayerSerializer(serializers.ModelSerializer):
    player = PlayerSerializer()
    class Meta:
        model = ClubePlayer
        fields = ['id','player', 'position','goals']
