from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import APIView, api_view
from .serializers import UserRegisterSerializer
from rest_framework import status


class UserRegisterView(APIView):
    def post(self, request):
        ser_data = UserRegisterSerializer(data=request.POST)
        if ser_data.is_valid():
            ser_data.create(ser_data.validated_data)
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)
