from django.shortcuts import render
from rest_framework import status
from rest_framework import viewsets
from . import serializers
from . import models
import requests #Python requests library used to get response from postalpincode api
from rest_framework.response import Response

# Create your views here.
class PinCodeViewSet(viewsets.ViewSet):
    serializer_class=serializers.PinCodeSerializer
    def list(self,request):
        return Response({'status':'OK'})

    def create(self,request):
        serializer=serializers.PinCodeSerializer(data=request.data)
        if serializer.is_valid():
                pincode=serializer.data.get('pincode')# getting data from pincode field
                url="https://api.postalpincode.in/pincode/"+str(pincode)
                response=requests.get(url)
                if response.json()[0]['PostOffice']==None:# if no records found for entered pincode
                    return Response({'message':"Invalid Pin Code"},status=status.HTTP_400_BAD_REQUEST)
                else:
                    places=[]# empty list to store all places having pincode
                    state=response.json()[0]['PostOffice'][0]['State']#accesing state returned by pincode
                    for i in response.json()[0]['PostOffice']:
                        places.append(i['Name'])# Storing name of all places one by one
                    return Response({'State':state,'Places':places})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
