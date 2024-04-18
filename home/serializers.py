from rest_framework import serializers


class PersonSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    age = serializers.IntegerField(required=True)