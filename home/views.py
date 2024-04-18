from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from .models import Person
from rest_framework.response import Response
from rest_framework.decorators import APIView, api_view
from .serializers import PersonSerializer


class HomeView(APIView):
    def get(self, request):
        person = Person.objects.all()
        ser_data = PersonSerializer(instance=person, many=True)
        return Response(ser_data.data)
