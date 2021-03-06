"""
__Seed builder__v0.1.8
  AUTO_GENERATED (Read only)
  Modify via builder
"""
from rest_framework import serializers
from dynamic_rest.fields import DynamicRelationField
from seed.helpers.serializer import Serializer
from app.models import Match
from app.models import Team

class _MatchSerializer(Serializer):  #
    
    local = DynamicRelationField('app.serializers.TeamSerializer', 
        deferred=True, embed=True, read_only=True)
    visitor = DynamicRelationField('app.serializers.TeamSerializer', 
        deferred=True, embed=True, read_only=True)
    scores = DynamicRelationField('app.serializers.ScoreSerializer',deferred=True, embed=True, many=True, read_only=True)

    score_ids = serializers.PrimaryKeyRelatedField(many=True, source='scores', read_only=True)

    local_id = serializers.PrimaryKeyRelatedField(source='local', queryset=Team.objects.all(), 
        required=True, allow_null=False)
    visitor_id = serializers.PrimaryKeyRelatedField(source='visitor', queryset=Team.objects.all(), 
        required=True, allow_null=False)

    class Meta:
        model = Match
        fields = (
            'id',
            'hash',
            'date',
            'type',
            'local',
            'visitor',
            'scores',
            'local_id',
            'visitor_id',
            'score_ids',  
        )
