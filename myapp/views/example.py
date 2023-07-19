from django.views.generic import TemplateView
from django.shortcuts import render


class HelloTemplateView(TemplateView):
    template_name = "my_web_app.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["my_name"] = "유광종"
        return context


class JqueryTemplateView(TemplateView):
    template_name = "jquery_study.html"


def jquery_page(request):
    return render(request, "jquery_study.html")
