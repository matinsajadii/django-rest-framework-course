from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from .models import Person, Question, Answer
from rest_framework.response import Response
from rest_framework.decorators import APIView, api_view
from .serializers import PersonSerializer, QuestionSerializer, AnswerSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework import status


class HomeView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        person = Person.objects.all()
        ser_data = PersonSerializer(instance=person, many=True)
        return Response(ser_data.data)


class QuestionView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        question = Question.objects.all()
        ser_data = QuestionSerializer(instance=question, many=True).data
        return Response(ser_data, status=status.HTTP_200_OK)

    def post(self, request):
        ser_data = QuestionSerializer(data=request.data)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        question = Question.objects.get(pk=pk)
        ser_data = QuestionSerializer(instance=question, data=request.data, partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        question = Question.objects.get(pk=pk)
        question.delete()
        return Response({"message":{"question deleted successfully"}})