from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ContactModel
from .serializers import ContactSerializer
from rest_framework import status

# Create your views here.
class Contactview(APIView):
    def get(self,req):
        data = {'message':"No get method used for Contact form"}
        return Response(data)
    
    def post(self,req):
        data = req.data
        serializer = ContactSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message" : "created successfully"},status=status.HTTP_201_CREATED)
        return Response (serializer.errors)
    

    # {"name":"sabari","email":"saba@12gmail.com" , "message":"heloooo"}
    