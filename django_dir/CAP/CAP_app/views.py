from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from CAP_app.models import Company
from CAP_app.serializers import *
from CAP_app.services import *


# Create your views here.


class CompanyHomeAPIView(APIView):
    def get(self, request):
        company = CompanyService.get_company()
        companySerializer = CompanySerializer(company)
        return Response(companySerializer.data)
class MainHomeAPIView(APIView):
    def get(self, request):
        active_employees, active_machinerys, active_foremans = ActiveObjService.get_active()
        return Response({"active_employees": active_employees,
                         "active_machinerys": active_machinerys,
                         "active_foremans": active_foremans})

class ObjectAPIView(APIView):
    def get(self, request):
        objects = ObjectService.get_objects()
        objectsSerializer = ObjectSerializer(objects, many=True)
        return Response(objectsSerializer.data)
    def patch(self, request):
        data = request.data
        object = ObjectService.update_object(data)
        return Response(ObjectSerializer(object).data)

class EmployeeAPIView(APIView):
    def get(self, request):
        employees, foremans, bracelets = EmployeeService.get_employees()
        Response(
            {
                "employees": EmployeeSerializer(employees, many=True).data,
                "foremans": ForemanSerializer(foremans, many=True).data,
                "bracelets": BraceletSerializer(bracelets, many=True).data,
            }
        )

    def post(self, request):
        data = request.data
        updated_data = EmployeeService.add_bracelet(data)
        if data['role'] == "Бригадир":
            return Response(ForemanSerializer(updated_data).data)
        else:
            return Response(EmployeeSerializer(updated_data).data)

    def delete(self, request):
        data = request.data
        updated_data = EmployeeService.delete_bracelet(data)
        if data['role'] == "Бригадир":
            return Response(ForemanSerializer(updated_data).data)
        else:
            return Response(EmployeeSerializer(updated_data).data)

class BraceletAPIView(APIView):
    def get(self, request):
        bracelets = BraceletService.get_bracelets()
        return Response(BraceletSerializer(bracelets, many=True).data)
    def post(self, request):
        bracelet = BraceletService.add_bracelet()
        return Response(BraceletSerializer(bracelet).data)
    def delete(self, request):
        data = request.data
        bracelet = BraceletService.delete_bracelet(data)
        return Response(BraceletSerializer(bracelet).data)


class ChipAPIView(APIView):
    def get(self, request):
        chip = ChipService.get_chip()
        return Response(ChipSerializer(chip, many=True).data)

    def post(self, request):
        chip = ChipService.add_chip()
        return Response(ChipSerializer(chip).data)

    def delete(self, request):
        data = request.data
        chip = ChipService.delete_chip(data)
        return Response(ChipSerializer(chip).data)
