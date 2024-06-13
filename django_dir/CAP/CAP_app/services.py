import random
import string
from datetime import date

from CAP_app.models import Company, Object, Employee, Machinery, Foreman, Bracelet, Chip


class CompanyService:

    @classmethod
    def get_company(self):
        company = Company.objects.get(id=1)
        return company

class ActiveObjService:
    @classmethod
    def get_active(self):
        company = Company.objects.get(id=1)
        active_foremans = len(Foreman.objects.filter(company=company, object__isnull=False))
        active_employees = len(Employee.objects.filter(object__isnull=False, company=company)) + active_foremans
        active_machinerys = len(Machinery.objects.filter(company=company, is_work=True))
        return active_employees, active_machinerys, active_foremans

class ObjectService:
    @classmethod
    def get_objects(cls):
        for i in range(10):
            Object.objects.create(company=Company.objects.get(pk=1),name="GG",start_time=date.today(), end_time=date.today(), x=1.1, y=2.2, radius=random.randint(0,10)).save()
        objects = Object.objects.all()
        return objects
    @classmethod
    def update_object(cls, data):
        object = Object.objects.filter(pk=data["id"])
        object.update(**data)
        return object


class EmployeeService:
    def get_employees(self):
        foremans = Foreman.objects.all()
        employees = Employee.objects.all()
        bracelets = Bracelet.objects.all()
        return employees, foremans, bracelets

    def add_bracelet(self, data):
        if data["role"] == "Бригадир":
            foreman = Foreman.object.get(pk=data["id"])
            foreman.update(bracelet=Bracelet.objects.get(pk=data["bracelet_id"]))
            return foreman
        else:
            employee = Employee.object.get(pk=data["id"])
            employee.update(bracelet=Bracelet.objects.get(pk=data["bracelet_id"]))
            return employee

    def delete_bracelet(self, data):
        if data["role"] == "Бригадир":
            foreman = Foreman.object.get(pk=data["id"])
            foreman.update(bracelet=None)
            return foreman
        else:
            employee = Employee.object.get(pk=data["id"])
            employee.update(bracelet=None)
            return employee

class BraceletService:
    def random_rfid(self, length):
        letters = string.ascii_letters + string.digits + string.punctuation  # добавляет буквы, цифры и специальные символы
        rfid = ''.join(random.choice(letters) for i in range(length))
        return rfid
    @classmethod
    def get_bracelets(self):
        bracelets = Bracelet.objects.all()
        return bracelets


    @classmethod
    def add_bracelet(self):
        rfid = self.random_rfid(10)
        bracelet = Bracelet(rfid=rfid, in_use=False)
        bracelet.save()
        return bracelet

    @classmethod
    def delete_bracelet(self, data):
        bracelet = Bracelet.objects.get(pk=data['id'])
        bracelet.delete()
        return bracelet


class ChipService:
    def random_chip_number(self, length):
        letters = string.ascii_letters + string.digits + string.punctuation  # добавляет буквы, цифры и специальные символы
        chip_number = ''.join(random.choice(letters) for i in range(length))
        return chip_number
    @classmethod
    def get_chip(self):
        chip = Chip.objects.all()
        return chip


    @classmethod
    def add_chip(self):
        chip_number = self.random_chip_number(10)
        chip = Chip(chip_number=chip_number, in_use=False)
        chip.save()
        return chip

    @classmethod
    def delete_chip(self, data):
        chip = Chip.objects.get(pk=data['id'])
        chip.delete()
        return chip

