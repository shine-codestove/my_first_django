from django.db import models
from rest_framework import serializers


# Create your models here.
class Person(models.Model):
    class Meta:
        db_table = "person"

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    sex = models.CharField(
        max_length=20, choices=(("male", "남"), ("female", "여")), default=""
    )


class PersonSerializer(serializers.Serializer):
    class Meta:
        model = Person

    first_name = serializers.CharField()
    last_name = serializers.CharField()
    age = serializers.IntegerField()
    sex = serializers.CharField()
