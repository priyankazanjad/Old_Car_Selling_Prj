from django.test import TestCase
from .models import Car
from django.urls import reverse

class CarTestCase(TestCase):
    def setUp(self):
        Car.objects.create(id=44,seller_name='radha',seller_mobile='7890543267',make='abc',model='aaa',year='2020',condition='good',price=5,is_buy=True)
        Car.objects.create(id=99,seller_name='preeti',seller_mobile='9590543267',make='xyz',model='zzz',year='2020',condition='good',price=8,is_buy=False)

    def test_car(self):
        qs = Car.objects.all()
        self.assertEqual(qs.count(),2)
        e1 = Car.objects.get(seller_name = 'radha')
        e2 = Car.objects.get(seller_name = 'preeti')
        self.assertNotEqual(e1.abcd(), '7895529060')
        self.assertNotEqual(e2.abcd(), '9595529060')



