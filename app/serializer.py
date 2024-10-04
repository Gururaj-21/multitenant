from rest_framework import serializers
from .models import Client, Domain

# Client Serializer
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'  # Include all fields or specify certain fields

# Domain Serializer
class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = '__all__'  # Include all fields or specify certain fields
