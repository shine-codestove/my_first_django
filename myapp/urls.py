from django.urls import path

from myapp.views import PersonView

app_name = "myapp"

urlpatterns = [
    path("person/", PersonView.as_view(), name="person_list_create"),
    path("person/<int:pk>/", PersonView.as_view(), name="person_detail_update_delete"),
]
