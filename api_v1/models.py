from django.db import models

# Create your models here.


class RawData(models.Model):
    date = models.DateField()
    s = models.CharField(max_length=32)
    x1 = models.FloatField()
    x2 = models.FloatField()
    x3 = models.FloatField()
    x4 = models.FloatField()
    x5 = models.FloatField()
    x6 = models.FloatField()
    x7 = models.FloatField()
    x8 = models.FloatField()
    x9 = models.FloatField()
    x10 = models.FloatField()
    x11 = models.FloatField()
    x12 = models.FloatField()
    x13 = models.FloatField()
    x14 = models.FloatField()
    x15 = models.FloatField()


class Feature(models.Model):
    date = models.OneToOneField(RawData, on_delete=models.CASCADE, related_name='feature_dates')
    s = models.OneToOneField(RawData, on_delete=models.CASCADE, related_name='feature_s')
    feature1 = models.FloatField()
    feature2 = models.FloatField()


class Prediction(models.Model):
    date = models.OneToOneField(RawData, on_delete=models.CASCADE, related_name='prediction_dates')
    s = models.OneToOneField(RawData, on_delete=models.CASCADE, related_name='prediction_ss')
    target = models.FloatField(null=True)
    prediction = models.FloatField(null=True)
