from rest_framework import serializers

from basic_app import models


class Kasalliklar(serializers.ModelSerializer):
    class Meta:
        model = models.Болезни1
        fields = '__all__'
