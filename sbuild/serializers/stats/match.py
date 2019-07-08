"""
__Seed builder__v1.0
  (Read_only) Modify via SeedManifest.yaml
"""

from rest_framework import serializers
from sbuild.helpers.serializer import Serializer
from models.stats.match import Match
from models.team import Team
from models.stats.score import Score
from models.helpers.file import File

from serializers.helpers.file import FileSerializer
from dynamic_rest.fields import DynamicRelationField

class _MatchSerializer(Serializer):  #
    
    local = DynamicRelationField('serializers.team.TeamSerializer', 
        deferred=True, embed=True, read_only=True)
    visitor = DynamicRelationField('serializers.team.TeamSerializer', 
        deferred=True, embed=True, read_only=True)
    scores = DynamicRelationField('serializers.stats.score.ScoreSerializer', 
        deferred=True, embed=True, many=True, read_only=True)

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
