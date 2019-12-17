from django.shortcuts import render
from rest_framework import viewsets
from api_v1.serializers import RawDataSerializer, FeatureSerializer, PredictionSerializer
from api_v1.models import RawData, Feature, Prediction

# Create your views here.


class RawDataViewSet(viewsets.ModelViewSet):
    queryset = RawData.objects.all().order_by('-date')
    serializer_class = RawDataSerializer


class FeatureViewSet(viewsets.ModelViewSet):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer


class PredictionViewSet(viewsets.ModelViewSet):
    queryset = Prediction.objects.all()
    serializer_class = PredictionSerializer
