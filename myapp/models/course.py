from django.db import models

from myapp.models.student import Student


class Course(models.Model):
    class Meta:
        db_table = "course"

    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    professor = models.CharField(max_length=100)
    limit = models.IntegerField(default=0)
    description = models.CharField(max_length=300)
    permit_subject = models.JSONField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class StudentCourse(models.Model):
    class Meta:
        db_table = "student_course"

    student = models.ForeignKey(
        Student, related_name="student", on_delete=models.CASCADE
    )
    course = models.ForeignKey(Course, related_name="course", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
