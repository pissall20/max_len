from api_v1.models import RawData, Feature
from api_v1.serializers import FeatureSerializer
from max_len.celery import app


@app.task(bind=True)
def create_features(raw_data_id):
    data_obj = RawData.objects.get(id=raw_data_id)

    features = raw_to_features(data_obj)

    feature_obj = Feature.objects.create(
        raw=data_obj,
        feature1=features['feature1'],
        feature2=features['feature2']
    )
    feature_obj.save()

    return FeatureSerializer(feature_obj)


def raw_to_features(raw):
    feature1 = raw.x1 + raw.x2
    feature2 = raw.x3 + raw.x4
    return {
        "feature1": feature1,
        "feature2": feature2
    }
