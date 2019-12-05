import datetime

from django.test import TestCase

from api_v1.models import RawData


class RawDataTestCase(TestCase):
    data = [{'date': datetime.datetime(2019, 12, 5, 23, 36, 25, 793802), 's': 'sh600000', 'x1': 1.8595, 'x2': 1.3029,
             'x3': 0.8252,
             'x4': 0.9083, 'x5': 0.4057, 'x6': -1.1732, 'x7': -0.3601, 'x8': -0.6425, 'x9': -0.3986, 'x10': 0.7965,
             'x11': 1.0632, 'x12': 0.7869, 'x13': 1.069, 'x14': 0.785, 'x15': 0.9099},
            {'date': datetime.datetime(2019, 12, 5, 23, 36, 46, 691925), 's': 'sh600004', 'x1': 0.7995, 'x2': 1.4682,
             'x3': 0.6751,
             'x4': -0.9422, 'x5': -1.2356, 'x6': 0.7951, 'x7': -0.1965, 'x8': 0.6358, 'x9': 0.7772, 'x10': -0.6514,
             'x11': -1.1367, 'x12': 0.715, 'x13': 1.1825, 'x14': 0.9326, 'x15': -0.5417},
            {'date': datetime.datetime(2019, 12, 5, 23, 37, 2, 261974), 's': 'sh600005', 'x1': 1.4422, 'x2': 1.8271,
             'x3': -0.9878,
             'x4': -0.2551, 'x5': 0.2915, 'x6': -0.3711, 'x7': 0.10300000000000001, 'x8': -0.3633, 'x9': -0.4838,
             'x10': -0.0812, 'x11': -0.349, 'x12': 0.5577, 'x13': -0.8423, 'x14': -0.2095, 'x15': -0.6638}]

    def test_raw_data(self):
        self.assertEquals(RawData.objects.count(), 0)
        RawData.objects.create(**self.data[0])
        RawData.objects.create(**self.data[1])
        self.assertEquals(RawData.objects.count(), 2)
