from django.db import models


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
