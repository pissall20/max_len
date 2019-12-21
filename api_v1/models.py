from django.db import models

# Create your models here.


class RawData(models.Model):
    date = models.DateField(null=False)
    s = models.CharField(max_length=32, null=False)
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

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['s', 'date'], name='serial_and_date')
        ]

    def __unicode__(self):
        return str(self.s) + "-" + str(self.date)


class Feature(models.Model):
    raw = models.OneToOneField(RawData, on_delete=models.CASCADE, primary_key=True, null=False)
    feature1 = models.FloatField(null=True)
    feature2 = models.FloatField(null=True)


class Target(models.Model):
    raw = models.OneToOneField(RawData, on_delete=models.CASCADE, primary_key=True, null=False)
    target = models.FloatField(null=True)


class Prediction(models.Model):
    raw = models.OneToOneField(RawData, on_delete=models.CASCADE, primary_key=True, null=False)
    prediction = models.FloatField(null=True)

