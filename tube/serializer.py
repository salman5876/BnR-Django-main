from rest_framework import serializers

from .models import *


class ShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Short
        fields = '__all__'
