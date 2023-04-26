from rest_framework import serializers
from .models import login,Secondary

class subscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = login
        fields = '__all__'

class secondarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Secondary
        fields = '__all__'