"""my_first_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.shortcuts import render
from django.urls import include, path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from rest_framework import routers

from myapp.views.person import PersonViewSet
from myapp.views.user import UserViewSet, GroupViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'persons', PersonViewSet)


def index(request):
    return render(request, 'index.html')


urlpatterns = [
    path("", index, name='index'),
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("myapp/", include("myapp.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
