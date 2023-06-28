from django.urls import path

from myapp.views import PersonView

app_name = "myapp"

urlpatterns = [
    path("person/", PersonView.as_view(), name="person_list_create"),
    path("person/<int:pk>/", PersonView.as_view(), name="person_detail_update_delete"),
    # path("person/", PersonView.as_view(), name="person_create"),
    # path("person/<int:pk>/update/", PersonView.as_view(), name="person_update"),
    # path("person/<int:pk>/", PersonView.as_view(), name="person_delete"),
    # path("people/", PersonListView.as_view(), name="people"),
]
