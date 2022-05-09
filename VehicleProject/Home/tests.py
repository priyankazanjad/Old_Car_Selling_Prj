from django.test import TestCase
from Home.models import Enquiry

class CarTestCase(TestCase):
    def setUp(self):
        Enquiry.objects.create(name='c', mobile= '9195529060')
        Enquiry.objects.create(name='x', mobile= '4595529060')

    def test_enquiry(self):
        qs = Enquiry.objects.all()
        self.assertEqual(qs.count(),2)
        e1 = Enquiry.objects.get(name = 'c')
        e2 = Enquiry.objects.get(name = 'x')
        self.assertNotEqual(e1.abcd(), '9195529060')
        self.assertNotEqual(e2.abcd(), '4595529060')


# Create your tests here.
