from rest_framework import serializers
from .models import Question, Answer

class PersonSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    age = serializers.IntegerField(required=True)


class QuestionSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = "__all__"

    def get_answers(self, obj):
        result = obj.answers.all()
        return AnswerSerializer(result, many=True).data


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"