from .serializers import ServerDetailsSerializer
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.

#For one API Permission
class GetServerDetails(APIView):
    #permission_classes = (IsAuthenticated,)

    def get(self, request):
        qs = ServerInventory.objects.filter(os_type='Linux')
        ser = ServerDetailsSerializer(qs, many=True)

        return Response(ser.data)

#For All API Permission
# class GetServerDetails(APIView):

#     def get(self, request):
#         qs = ServerInventory.objects.filter(os_type='Linux')
#         ser = ServerDetailsSerializer(qs, many=True)

#         return Response(ser.data)

#For Global API Permission
class GetServerDetailsApi2(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        qs = ServerInventory.objects.filter(os_type='Linux')
        ser = ServerDetailsSerializer(qs, many=True)

        return Response(ser.data)
        
