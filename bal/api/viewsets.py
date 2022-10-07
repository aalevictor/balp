from bal import models
from bal.api import serializers
from rest_framework import viewsets


class PlayerViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PlayerSerializer
    queryset = models.Player.objects.all()

class TechnicalViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TechnicalSerializer
    queryset = models.Technical.objects.all()

class GoalkeeperViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.GoalkeeperSerializer
    queryset = models.Goalkeeper.objects.all()
