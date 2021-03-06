"""
__Seed builder__v0.1.8
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene
import random
from graphene import ObjectType
from graphene_django.types import DjangoObjectType
from seed.schema.util.query_util import parse_query
from app.models import Match as MatchModel
from app.models import Player as PlayerModel
from app.models import PlayerPosition as PlayerPositionModel
from app.models import Score as ScoreModel
from app.models import Team as TeamModel
from app.models import User as UserModel
from app.models import File as FileModel

class Match(DjangoObjectType):
    class Meta:
        model = MatchModel
        description = "Represents a match between two teams  (A vs B)"

class MatchCount(ObjectType):
    id = graphene.Int()
    count = graphene.Int()

class Player(DjangoObjectType):
    class Meta:
        model = PlayerModel

class PlayerCount(ObjectType):
    id = graphene.Int()
    count = graphene.Int()

class PlayerPosition(DjangoObjectType):
    class Meta:
        model = PlayerPositionModel
        description = "Represents a player  position (eg. forward)"

class PlayerPositionCount(ObjectType):
    id = graphene.Int()
    count = graphene.Int()

class Score(DjangoObjectType):
    class Meta:
        model = ScoreModel
        description = "Represents a match score (goal)"

class ScoreCount(ObjectType):
    id = graphene.Int()
    count = graphene.Int()

class Team(DjangoObjectType):
    class Meta:
        model = TeamModel

class TeamCount(ObjectType):
    id = graphene.Int()
    count = graphene.Int()

class User(DjangoObjectType):
    class Meta:
        model = UserModel
        exclude = ('password',)
        description = "Represents a registered user"

class UserCount(ObjectType):
    id = graphene.Int()
    count = graphene.Int()

class File(DjangoObjectType):
    class Meta:
        model = FileModel
        description = 'Represents a File object'

class FileCount(ObjectType):
    id = graphene.Int()
    count = graphene.Int()

class Query(object):
    
    matches = graphene.List(Match, query=graphene.String(), orderBy=graphene.String(),
      start=graphene.Int(), end=graphene.Int())
    matchCount = graphene.Field(MatchCount, query=graphene.String())
    match = graphene.Field(Match, id=graphene.Int())
    players = graphene.List(Player, query=graphene.String(), orderBy=graphene.String(),
      start=graphene.Int(), end=graphene.Int())
    playerCount = graphene.Field(PlayerCount, query=graphene.String())
    player = graphene.Field(Player, id=graphene.Int())
    playerPositions = graphene.List(PlayerPosition, query=graphene.String(), orderBy=graphene.String(),
      start=graphene.Int(), end=graphene.Int())
    playerPositionCount = graphene.Field(PlayerPositionCount, query=graphene.String())
    playerPosition = graphene.Field(PlayerPosition, id=graphene.Int())
    scores = graphene.List(Score, query=graphene.String(), orderBy=graphene.String(),
      start=graphene.Int(), end=graphene.Int())
    scoreCount = graphene.Field(ScoreCount, query=graphene.String())
    score = graphene.Field(Score, id=graphene.Int())
    teams = graphene.List(Team, query=graphene.String(), orderBy=graphene.String(),
      start=graphene.Int(), end=graphene.Int())
    teamCount = graphene.Field(TeamCount, query=graphene.String())
    team = graphene.Field(Team, id=graphene.Int())
    users = graphene.List(User, query=graphene.String(), orderBy=graphene.String(),
      start=graphene.Int(), end=graphene.Int())
    userCount = graphene.Field(UserCount, query=graphene.String())
    user = graphene.Field(User, id=graphene.Int())
    files = graphene.List(File, query=graphene.String(), orderBy=graphene.String(),
      start=graphene.Int(), end=graphene.Int())
    file = graphene.Field(File, id=graphene.Int())
    fileCount = graphene.Field(FileCount, query=graphene.String())

    def resolve_matches(self, info, **kwargs):
        if "query" in kwargs:
            res = parse_query(kwargs["query"], MatchModel)
        else: res = MatchModel.objects.all()
        if "orderBy" in kwargs:
            orders = kwargs["orderBy"].split(",")
            for order in orders:
              res = res.order_by(order)
        if "start" in kwargs and "end" not in kwargs:
            res = res[kwargs["start"]:]
        if "end" in kwargs and "start" not in kwargs:
            res = res[:kwargs["end"]]
        if "start" in kwargs and "end" in kwargs:
            res = res[kwargs["start"]:kwargs["end"]]
        return res

    def resolve_matchCount(self, info, **kwargs):
        if "query" in kwargs:
            return MatchCount(
                id = random.randint(0, 1000000),
                count=len(parse_query(kwargs["query"], MatchModel)))
        else:
            return MatchCount(
                id = random.randint(0, 1000000),
                count=len(MatchModel.objects.all()))

    def resolve_match(self, info, id):
        return MatchModel.objects.get(pk=id)
    
    def resolve_players(self, info, **kwargs):
        if "query" in kwargs:
            res = parse_query(kwargs["query"], PlayerModel)
        else: res = PlayerModel.objects.all()
        if "orderBy" in kwargs:
            orders = kwargs["orderBy"].split(",")
            for order in orders:
              res = res.order_by(order)
        if "start" in kwargs and "end" not in kwargs:
            res = res[kwargs["start"]:]
        if "end" in kwargs and "start" not in kwargs:
            res = res[:kwargs["end"]]
        if "start" in kwargs and "end" in kwargs:
            res = res[kwargs["start"]:kwargs["end"]]
        return res

    def resolve_playerCount(self, info, **kwargs):
        if "query" in kwargs:
            return PlayerCount(
                id = random.randint(0, 1000000),
                count=len(parse_query(kwargs["query"], PlayerModel)))
        else:
            return PlayerCount(
                id = random.randint(0, 1000000),
                count=len(PlayerModel.objects.all()))

    def resolve_player(self, info, id):
        return PlayerModel.objects.get(pk=id)
    
    def resolve_playerPositions(self, info, **kwargs):
        if "query" in kwargs:
            res = parse_query(kwargs["query"], PlayerPositionModel)
        else: res = PlayerPositionModel.objects.all()
        if "orderBy" in kwargs:
            orders = kwargs["orderBy"].split(",")
            for order in orders:
              res = res.order_by(order)
        if "start" in kwargs and "end" not in kwargs:
            res = res[kwargs["start"]:]
        if "end" in kwargs and "start" not in kwargs:
            res = res[:kwargs["end"]]
        if "start" in kwargs and "end" in kwargs:
            res = res[kwargs["start"]:kwargs["end"]]
        return res

    def resolve_playerPositionCount(self, info, **kwargs):
        if "query" in kwargs:
            return PlayerPositionCount(
                id = random.randint(0, 1000000),
                count=len(parse_query(kwargs["query"], PlayerPositionModel)))
        else:
            return PlayerPositionCount(
                id = random.randint(0, 1000000),
                count=len(PlayerPositionModel.objects.all()))

    def resolve_playerPosition(self, info, id):
        return PlayerPositionModel.objects.get(pk=id)
    
    def resolve_scores(self, info, **kwargs):
        if "query" in kwargs:
            res = parse_query(kwargs["query"], ScoreModel)
        else: res = ScoreModel.objects.all()
        if "orderBy" in kwargs:
            orders = kwargs["orderBy"].split(",")
            for order in orders:
              res = res.order_by(order)
        if "start" in kwargs and "end" not in kwargs:
            res = res[kwargs["start"]:]
        if "end" in kwargs and "start" not in kwargs:
            res = res[:kwargs["end"]]
        if "start" in kwargs and "end" in kwargs:
            res = res[kwargs["start"]:kwargs["end"]]
        return res

    def resolve_scoreCount(self, info, **kwargs):
        if "query" in kwargs:
            return ScoreCount(
                id = random.randint(0, 1000000),
                count=len(parse_query(kwargs["query"], ScoreModel)))
        else:
            return ScoreCount(
                id = random.randint(0, 1000000),
                count=len(ScoreModel.objects.all()))

    def resolve_score(self, info, id):
        return ScoreModel.objects.get(pk=id)
    
    def resolve_teams(self, info, **kwargs):
        if "query" in kwargs:
            res = parse_query(kwargs["query"], TeamModel)
        else: res = TeamModel.objects.all()
        if "orderBy" in kwargs:
            orders = kwargs["orderBy"].split(",")
            for order in orders:
              res = res.order_by(order)
        if "start" in kwargs and "end" not in kwargs:
            res = res[kwargs["start"]:]
        if "end" in kwargs and "start" not in kwargs:
            res = res[:kwargs["end"]]
        if "start" in kwargs and "end" in kwargs:
            res = res[kwargs["start"]:kwargs["end"]]
        return res

    def resolve_teamCount(self, info, **kwargs):
        if "query" in kwargs:
            return TeamCount(
                id = random.randint(0, 1000000),
                count=len(parse_query(kwargs["query"], TeamModel)))
        else:
            return TeamCount(
                id = random.randint(0, 1000000),
                count=len(TeamModel.objects.all()))

    def resolve_team(self, info, id):
        return TeamModel.objects.get(pk=id)
    
    def resolve_users(self, info, **kwargs):
        if "query" in kwargs:
            res = parse_query(kwargs["query"], UserModel)
        else: res = UserModel.objects.all()
        if "orderBy" in kwargs:
            orders = kwargs["orderBy"].split(",")
            for order in orders:
              res = res.order_by(order)
        if "start" in kwargs and "end" not in kwargs:
            res = res[kwargs["start"]:]
        if "end" in kwargs and "start" not in kwargs:
            res = res[:kwargs["end"]]
        if "start" in kwargs and "end" in kwargs:
            res = res[kwargs["start"]:kwargs["end"]]
        return res

    def resolve_userCount(self, info, **kwargs):
        if "query" in kwargs:
            return UserCount(
                id = random.randint(0, 1000000),
                count=len(parse_query(kwargs["query"], UserModel)))
        else:
            return UserCount(
                id = random.randint(0, 1000000),
                count=len(UserModel.objects.all()))

    def resolve_user(self, info, id):
        return UserModel.objects.get(pk=id)
    
    def resolve_files(self, info, **kwargs):
        if "query" in kwargs:
            res = parse_query(kwargs["query"], FileModel)
        else: res = FileModel.objects.all()
        if "orderBy" in kwargs:
            orders = kwargs["orderBy"].split(",")
            for order in orders:
              res = res.order_by(order)
        if "start" in kwargs and "end" not in kwargs:
            res = res[kwargs["start"]:]
        if "end" in kwargs and "start" not in kwargs:
            res = res[:kwargs["end"]]
        if "start" in kwargs and "end" in kwargs:
            res = res[kwargs["start"]:kwargs["end"]]
        return res

    def resolve_fileCount(self, info, **kwargs):
        if "query" in kwargs:
            return FileCount(
                id = 0,
                count=len(parse_query(kwargs["query"], FileModel)))
        else:
            return FileCount(
                id = 0,
                count=len(FileModel.objects.all()))

    def resolve_file(self, info, id):
        return FileModel.objects.get(pk=id)