from bal import models
from rest_framework import serializers


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Player
        fields = '__all__'

class TechnicalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Technical
        fields = '__all__'

class GoalkeeperSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Goalkeeper
        fields = '__all__'
