from django.urls import path

from myapp.views.example import HelloTemplateView, JqueryTemplateView
from myapp.views.person import (
    PersonView,
    PersonTemplateView,
)
from myapp.views.student import (
    StudentCourseView,
    StudentTemplateView,
    StudentListTemplateView,
    StudentView,
)

app_name = "myapp"

urlpatterns = [
    path("person/", PersonView.as_view(), name="person_list_create"),
    path("person/<int:pk>/", PersonView.as_view(), name="person_detail_update_delete"),
    path("person/view/", PersonTemplateView.as_view(), name="person_template"),
    path("student/", StudentView.as_view(), name="student_list"),
    path("student/<int:pk>", StudentView.as_view(), name="student_get"),
    path(
        "student/<int:st_id>/course/",
        StudentCourseView.as_view(),
        name="student_course_get",
    ),
    path(
        "student/list_page/",
        StudentListTemplateView.as_view(),
        name="student_list_page",
    ),
    path(
        "student/page/",
        StudentTemplateView.as_view(),
        name="student_page",
    ),
    path("geolocation/", HelloTemplateView.as_view(), name="geolocation_detail_page"),
    path("jquery/", JqueryTemplateView.as_view(), name="jquery_study"),
    path("hello/", HelloTemplateView.as_view(), name="hello_template"),
]
