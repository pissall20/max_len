from rest_framework import serializers

from api_v1.models import RawData, Feature, Prediction
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'email', 'first_name', 'last_name',)


class RawDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawData
        fields = "__all__"


class FeatureSerializer(serializers.ModelSerializer):
    # Add raw data fields
    raw_data = RawDataSerializer(required=False, read_only=True)

    class Meta:
        model = Feature
        fields = "__all__"


class PredictionSerializer(serializers.ModelSerializer):
    # Add raw data fields
    raw_data = RawDataSerializer(required=False, read_only=True)

    class Meta:
        model = Prediction
        fields = "__all__"
