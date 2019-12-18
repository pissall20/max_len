from django.shortcuts import render
from rest_framework import viewsets, status
from api_v1.serializers import RawDataSerializer, FeatureSerializer, PredictionSerializer
from api_v1.models import RawData, Feature, Prediction
from rest_framework.response import Response

# Create your views here.


class RawDataViewSet(viewsets.ModelViewSet):
    queryset = RawData.objects.all().order_by('-date')
    serializer_class = RawDataSerializer

    def create(self, request, *args, **kwargs):
        many = True if isinstance(request.data, list) else False
        serializer = RawDataSerializer(data=request.data, many=many)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class FeatureViewSet(viewsets.ModelViewSet):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer


class PredictionViewSet(viewsets.ModelViewSet):
    queryset = Prediction.objects.all()
    serializer_class = PredictionSerializer
