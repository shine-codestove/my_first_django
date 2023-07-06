import json

from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from myapp.models.course import StudentCourse
from myapp.models.student import Student


class StudentCourseView(View):
    def get(self, request, st_id):
        student = Student.objects.filter(id=st_id).values().first()
        course_list = (
            StudentCourse.objects.filter(student_id=st_id)
            .select_related("course")
            .values()
        )

        return JsonResponse(
            {"student": student, "course_list": list(course_list)}, safe=False
        )


@method_decorator(csrf_exempt, name="dispatch")
class StudentView(View):
    # 단건조회(pk가 있는경우), 목록조회
    def get(self, request, pk=None):
        if pk is not None:
            # person = Person.objects.filter(id=pk).values()
            student = Student.objects.filter(id=pk).values().first()
            if not student:
                return JsonResponse({"error": "student not found"}, status=404)
            return JsonResponse(student)
        else:
            students = Student.objects.all()
            return JsonResponse(list(students.values()), safe=False)

    # 등록
    def post(self, request):
        data = json.loads(request.body)

        p = Student(
            name=data.get("name"),
            student_no=data.get("student_no"),
            grade=data.get("grade"),
            department=data.get("department"),
        )
        p.save()
        # return HttpResponse(status=200)
        return JsonResponse({"message": "저장이 완료되었습니다"}, status=200)


class StudentListTemplateView(TemplateView):
    template_name = "student_list.html"


def jquery_page(request):
    return render(request, "jquery_study.html")


class StudentTemplateView(TemplateView):
    template_name = "student.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["my_name"] = "유광종"
        student = Student.objects.filter(id=1).values().first()

        context["student"] = student
        return context
