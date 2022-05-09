from django.db import models

CONDITION = (
    ('good','good'),
    ('average','average'),
    ('poor','poor')
)
class Car(models.Model):
    id = models.IntegerField(primary_key=True)
    seller_name = models.CharField(max_length=30)
    seller_mobile = models.CharField(max_length=10)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.CharField(max_length=4)
    condition = models.CharField(max_length=60,choices=CONDITION)
    price = models.IntegerField()
    is_buy = models.BooleanField(default=False)


    def abcd(self):
        return f"{self.id},{ self.seller_name}"
