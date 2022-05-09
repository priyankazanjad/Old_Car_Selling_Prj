from django.db import models

class Enquiry(models.Model):

    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=10)

    def abcd(self):
        return f"{self.name},{self.mobile}"