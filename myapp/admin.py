from django.contrib import admin
from myapp.models.person import Person
from myapp.models.student import Student


class PersonAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
    )


admin.site.register(Person, PersonAdmin)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_no", "name")
