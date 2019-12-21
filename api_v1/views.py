from django.shortcuts import render
from rest_framework import viewsets, status
from api_v1.serializers import RawDataSerializer, FeatureSerializer, PredictionSerializer, TargetSerializer
from api_v1.models import RawData, Feature, Prediction, Target
from rest_framework.response import Response
import pandas as pd
from api_v1 import tasks
from joblib import dump, load
from django.db.utils import IntegrityError

# Create your views here.


class RawDataViewSet(viewsets.ModelViewSet):
    queryset = RawData.objects.all().order_by('-date')
    serializer_class = RawDataSerializer

    def create(self, request, *args, **kwargs):
        many = True if isinstance(request.data, list) else False
        serializer = RawDataSerializer(data=request.data, many=many)
        if serializer.is_valid():
            try:
                serializer.save()
            except IntegrityError as e:
                return Response({
                    str(e)
                }, status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        df = pd.DataFrame(request.data if isinstance(request.data, list) else [request.data])
        # feature_df = tasks.raw_to_features(df)

        model = load("api_v1/regr_model.joblib")
        feature_cols = [x for x in df.columns if x not in ["prediction", 'target', 'date', 's']]
        test_X = df[feature_cols]
        prediction_list = model.predict(test_X).tolist()

        for data_instance, prediction_instance in zip(serializer.instance, prediction_list):
            predict = Prediction(raw=data_instance, prediction=prediction_instance)
            predict.save()

        return Response({
            "raw_data": serializer.data,
            "prediction": prediction_list
        }, status=status.HTTP_201_CREATED)


class TargetViewSet(viewsets.ModelViewSet):
    queryset = Target.objects.all()
    serializer_class = TargetSerializer


class FeatureViewSet(viewsets.ModelViewSet):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer


class PredictionViewSet(viewsets.ModelViewSet):
    queryset = Prediction.objects.all()
    serializer_class = PredictionSerializer


class DoPredictViewSet(viewsets.ViewSet):

    def get(self, request):
        data = request.data
        data_id = data.get("id")
        pass

    def post(self, request):
        data = request.data
        pass


