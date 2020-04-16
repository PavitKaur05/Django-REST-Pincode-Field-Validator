from django.db import models

# Create your models here.
class PinCodeModel(models.Model):
    """Model to accept pincode"""
    pincode=models.PositiveIntegerField()

    def __str__(self):
        return self.pinCode
