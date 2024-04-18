from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import APIView, api_view
from .serializers import RegisterUserSerializer


class RegisterUserView(APIView):
    def post(self, request):
        ser_data = RegisterUserSerializer(data=request.POST)
        if ser_data.is_valid():
            User.objects.create_user(
                username=ser_data.validated_data["username"],
                email=ser_data.validated_data["email"],
                password=ser_data.validated_data["password"]
            )
            return Response(ser_data.data)
        
        return Response(ser_data.errors)
