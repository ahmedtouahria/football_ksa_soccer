from rest_framework import serializers
from club.models import *
from .models import *
from rest_framework.validators import UniqueTogetherValidator
from rest_framework.response import Response

class ClubeNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clube
        fields = ['name','logo']
class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ['id','clube_one','clube_two','score_one','score_two','time_start']

class HomeMatchsSerializer(serializers.ModelSerializer):
    clube_one = ClubeNameSerializer(many=False)
    clube_two = ClubeNameSerializer(many=False)
    class Meta:
        model = Match
        fields = '__all__'

class SendMatchOrderSerializer(serializers.ModelSerializer):
    match = MatchSerializer(many=False)
    class Meta:
        model = OrderArbitreMatch
        fields = ['match','price','status']
class SendMatchCardSerializer(serializers.ModelSerializer):
    match = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = MatchCard
        fields = ['match','card','player']
        extra_kwargs = {'match': {'required': False}}
        # Apply custom
class SendPLayerGoalSerializer(serializers.ModelSerializer):
    match = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = GoalMatch
        fields = ['player','match','is_penalty']
        extra_kwargs = {'match': {'required': False}}
        # Apply custom