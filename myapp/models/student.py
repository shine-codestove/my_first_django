from django.db import models


class Student(models.Model):
    class Meta:
        db_table = "student"

    GRADE_TYPE = (
        ("1", "1학년"),
        ("2", "2학년"),
        ("3", "3학년"),
        ("4", "4학년"),
        ("5", "5학년"),
    )

    student_no = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    grade = models.CharField(max_length=20, choices=GRADE_TYPE, default="1")
    department = models.CharField(max_length=100)
    courses = models.JSONField(default=dict)

    def __str__(self):
        return self.name
