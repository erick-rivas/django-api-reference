"""
__Seed builder__v0.1.8
  AUTO_GENERATED (Read only)
  Modify via builder
"""
from rest_framework import serializers
from dynamic_rest.fields import DynamicRelationField
from seed.helpers.serializer import Serializer
from app.models import Score
from app.models import Player
from app.models import Match

class _ScoreSerializer(Serializer):  #
    
    player = DynamicRelationField('app.serializers.PlayerSerializer', 
        deferred=True, embed=True, read_only=True)
    match = DynamicRelationField('app.serializers.MatchSerializer', 
        deferred=True, embed=True, read_only=True)

    player_id = serializers.PrimaryKeyRelatedField(source='player', queryset=Player.objects.all(), 
        required=True, allow_null=False)
    match_id = serializers.PrimaryKeyRelatedField(source='match', queryset=Match.objects.all(), 
        required=True, allow_null=False)

    class Meta:
        model = Score
        fields = (
            'id',
            'hash',
            'min',
            'player',
            'match',
            'player_id',
            'match_id',  
        )
