"""
__Seed builder__v1.0
  (Read_only) Modify via SeedManifest.yaml
"""

from datetime import datetime
from django.db import models
from models.helpers.model import Model

class _Team(Model):  #
    
    name = models.CharField(max_length=256, blank=True)
    logo = models.ForeignKey('File', related_name='team_logos', 
        blank=False, null=False, on_delete=models.CASCADE)
    description = models.TextField(blank=True, default="No description available")
    market_value = models.FloatField()
    identity_docs = models.ManyToManyField('File', related_name='team_identity_docs', blank=False)

    class Meta:
        abstract = True

