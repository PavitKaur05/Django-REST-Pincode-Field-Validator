from rest_framework import serializers
from . import models


def validPinCode(value):
    #A custom validator function for pincode field
    if (str(value).isdecimal()==False):
        raise serializers.ValidationError('This Pincode must contain only digits')
    if (len(str(value))!=6):
        raise serializers.ValidationError('This Pincode must contain 6 digits')


    return value


class PinCodeSerializer(serializers.Serializer):
    """A serializer for pin code"""
    pincode=serializers.CharField(validators=[validPinCode])
