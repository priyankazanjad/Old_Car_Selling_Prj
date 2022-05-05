from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

CONDITION = (
    ('good','good'),
    ('average','average'),
    ('poor','poor')
)
class Car(models.Model):
    id = models.IntegerField(primary_key=True)
    seller_name = models.CharField(max_length=30)
    seller_mobile = PhoneNumberField(null=False,blank=False)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.DateField()
    condition = models.CharField(max_length=60,choices=CONDITION)
    price = models.IntegerField()
    is_buy = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.seller_name}"
