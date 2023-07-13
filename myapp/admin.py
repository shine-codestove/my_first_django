from django.contrib import admin
from myapp.models.course import Course, StudentCourse
from myapp.models.person import Person
from myapp.models.price_file import PriceFile
from myapp.models.price_table import PriceTable
from myapp.models.student import Student


class PersonAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
    )


admin.site.register(Person, PersonAdmin)


@admin.register(PriceTable)
class PriceTableAdmin(admin.ModelAdmin):
    search_fields = ['start_area', 'end_area']
    list_display = ("id", "start_area", "end_area", "price")


@admin.register(PriceFile)
class PriceFileAdmin(admin.ModelAdmin):
    list_display = ("id", "file", "uploaded_at")


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "student_no", "name")


@admin.register(StudentCourse)
class StudentCourseAdmin(admin.ModelAdmin):
    list_display = ("id", "student", "course", "created_at")


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "code", "name", "professor")
