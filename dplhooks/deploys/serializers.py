from rest_framework import serializers


class DeploySerializer(serializers.Serializer):
    token = serializers.CharField(max_length=200)
    project = serializers.CharField(max_length=200)
