from rest_framework import serializers
from .models import Question, Answer
from .custom_relational_field import UserEmaliNameRelationalField


class PersonSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    age = serializers.IntegerField(required=True)


class QuestionSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()
    # user = serializers.StringRelatedField(read_only=True)
    # user = serializers.PrimaryKeyRelatedField(read_only=True)
    # user = serializers.SlugRelatedField(read_only=True, slug_field="email")
    user = UserEmaliNameRelationalField(read_only=True)


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