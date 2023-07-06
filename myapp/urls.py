from django.urls import path

from myapp.views import PersonView, PersonTemplateView, StudentCourseView

app_name = "myapp"

urlpatterns = [
    path("person/", PersonView.as_view(), name="person_list_create"),
    path("person/<int:pk>/", PersonView.as_view(), name="person_detail_update_delete"),
    path("person/view/", PersonTemplateView.as_view(), name="person_template"),
    path(
        "school/student_course/<int:st_id>/",
        StudentCourseView.as_view(),
        name="student_course_get",
    ),
]
