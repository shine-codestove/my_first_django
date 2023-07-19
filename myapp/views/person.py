import json

from django import forms
from django.http import (
    HttpResponse,
    JsonResponse,
)
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.viewsets import ModelViewSet

from myapp.models.person import Person, PersonSerializer


# DRF를 위한 ViewSet
class PersonViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = "__all__"


@method_decorator(csrf_exempt, name="dispatch")
class PersonView(View):
    form_class = PersonForm

    # 단건조회(pk가 있는경우), 목록조회
    def get(self, request, pk=None):
        if pk is not None:
            # person = Person.objects.filter(id=pk).values()
            person = Person.objects.filter(id=pk).values().first()
            if not person:
                return JsonResponse({"error": "Person not found"}, status=404)
            return JsonResponse(person)
        else:
            people = Person.objects.all()
            return JsonResponse(list(people.values()), safe=False)

    # 수정
    def put(self, request, pk):
        person = get_object_or_404(Person, pk=pk)
        data = json.loads(request.body)

        person.age = data.get("age") or person.age
        person.sex = data.get("sex") or person.sex
        person.first_name = data.get("first_name") or person.first_name
        person.last_name = data.get("last_name") or person.last_name

        person.save()
        return JsonResponse(data)

        # form = self.form_class(data, instance=person)
        # if form.is_valid():
        #     form.save()
        #     return JsonResponse(data)

        # return JsonResponse({"error": "입력값이 잘못 되었습니다."}, status=400)

    # 삭제
    def delete(self, request, pk):
        person = get_object_or_404(Person, pk=pk)
        person.delete()
        return HttpResponse(status=200)

    # 등록
    def post(self, request):
        data = json.loads(request.body)

        p = Person(
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            age=data.get("age"),
            sex=data.get("sex"),
        )
        p.save()
        # return HttpResponse(status=200)
        return JsonResponse({"message": "저장이 완료되었습니다"}, status=200)


class PersonTemplateView(TemplateView):
    template_name = "person_template.html"  # The path to your template file

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        person = Person.objects.first()
        context["person"] = person
        context["greeting"] = "Hello, world!"  # Adding a context variable
        return context

# class PersonListView(ListView):
#     model = Person
#     context_object_name = "persons"

#     def get_queryset(self):
#         queryset = super().get_queryset()

#         # request의 GET parameter에서 필터링할 값 가져오기
#         first_name = self.request.GET.get("first_name")

#         # 필터링 조건이 존재하는 경우에만 필터링 수행
#         if first_name:
#             queryset = queryset.filter(first_name=first_name)

#         return queryset

#     def render_to_response(self, context, **response_kwargs):
#         # 쿼리셋을 JSON 형식으로 변환
#         data = list(context["object_list"].values())

#         # JSON 응답 반환
#         return JsonResponse(data, safe=False)


# class PersonDetailView(DetailView):
#     model = Person

#     def render_to_response(self, context, **response_kwargs):
#         person = self.get_object()
#         data = {
#             "first_name": person.first_name,
#             "last_name": person.last_name,
#             "age": person.age,
#         }
#         # JSON 응답 반환
#         return JsonResponse(data)


# from django.views.generic.edit import CreateView


# @method_decorator(csrf_exempt, name="dispatch")
# class PersonCreateView(CreateView):
#     model = Person
#     fields = ["first_name", "last_name", "age"]

#     def render_to_response(self, context, **response_kwargs):
#         return HttpResponse(status=201)


# @method_decorator(csrf_exempt, name="dispatch")
# class PersonUpdateView(UpdateView):
#     model = Person
#     fields = ["first_name", "last_name", "age"]

#     def render_to_response(self, context, **response_kwargs):
#         return HttpResponse(status=200)


# /myapp/student_course/<int:st_no>/
# /myapp/student_course/1001/
