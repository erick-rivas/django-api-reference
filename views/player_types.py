"""
__Seed builder__v1.0
"""

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from seed.util.req_util import has_fields_or_400

from seed.views.player_types import _PlayerTypeViewSet
from app.models import PlayerType

class PlayerTypeViewSet(_PlayerTypeViewSet):  #
    pass