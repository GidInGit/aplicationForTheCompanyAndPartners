from django.urls import path

from CAP_app.views import *

urlpatterns = [
    path("company/", CompanyHomeAPIView.as_view(), name="home"),
    path("objects/", ObjectAPIView.as_view(), name="objects"),
    path("main/", MainHomeAPIView.as_view(), name="main"),
    path("employees/", EmployeeAPIView.as_view(), name="employees"),
    path("bracelets/", BraceletAPIView.as_view(), name="bracelets"),
    path("chips/", ChipAPIView.as_view(), name="chips"),
]