from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Enquiry(models.Model):

    name = models.CharField(max_length=50)
    mobile = PhoneNumberField(null=False,blank=False)

    def _str_(self):
        return f"{self.name},{self.mobile}"