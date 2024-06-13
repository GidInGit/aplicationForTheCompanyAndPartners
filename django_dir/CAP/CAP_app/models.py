from django.db import models

# Create your models here.




#CAP --------------------------->>>

class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

class Object(models.Model):
    id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    address = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    x = models.FloatField()
    y = models.FloatField()
    radius = models.FloatField()



class Partner(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    partner_description = models.TextField()
    services_description = models.TextField()

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    object = models.ForeignKey(Object, on_delete=models.CASCADE)
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    text = models.TextField()
    date_time = models.DateTimeField()


class Task_queue(models.Model):
    id = models.AutoField(primary_key=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    status = models.BooleanField()
    finished = models.BooleanField()


class Bracelet(models.Model):
    id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    rfid = models.CharField(max_length=50)
    in_use = models.BooleanField()

class Chip(models.Model):
    id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    chip_number = models.CharField()
    in_use = models.BooleanField()



class Foreman(models.Model):
    id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    object = models.ForeignKey(Object, on_delete=models.CASCADE, null=True)
    bracelet = models.ForeignKey(Bracelet, on_delete=models.CASCADE, null=True)
    role = models.CharField(max_length=50, default="Бригадир")
    full_name = models.CharField(max_length=50)


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    object = models.ForeignKey(Object, on_delete=models.CASCADE, null=True)
    bracelet = models.ForeignKey(Bracelet, on_delete=models.CASCADE, null=True)
    foreman = models.ForeignKey(Foreman, on_delete=models.CASCADE, null=True)
    full_name = models.TextField()
    role = models.TextField()

class Machinery(models.Model):
    id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    chip = models.ForeignKey(Chip, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    state_number = models.CharField(max_length=50)
    is_work = models.BooleanField()



#Analytics

class today_bracelet_stats(models.Model):
    id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    object = models.ForeignKey(Object, on_delete=models.CASCADE)
    pulse = models.BooleanField()
    timeout = models.FloatField()
    untraceable = models.FloatField()

class analytics_of_day_bracelet_stats(models.Model):
    id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    object = models.ForeignKey(Object, on_delete=models.CASCADE)
    first_entry_time = models.DateTimeField()
    last_exit_time = models.DateTimeField()
    total_timeout = models.FloatField()
    total_untraceable = models.FloatField()
    date = models.DateTimeField()


class today_machinery_stats(models.Model):
    id = models.AutoField(primary_key=True)
    machinery = models.ForeignKey(Machinery, on_delete=models.CASCADE)
    average_speed = models.FloatField()
    fuel_consumption = models.FloatField()
    engine_hours = models.FloatField()
    work_hours = models.FloatField()


class analytics_of_day_machinery_stats(models.Model):
    id = models.AutoField(primary_key=True)
    machinery = models.ForeignKey(Machinery, on_delete=models.CASCADE)
    total_average_speed = models.FloatField()
    total_fuel_consumption = models.FloatField()
    total_engine_hours = models.FloatField()
    total_work_hours = models.FloatField()
    date = models.DateTimeField()

class total_analytics_of_brigade(models.Model):
    id = models.AutoField(primary_key=True)
    foreman = models.ForeignKey(Foreman, on_delete=models.CASCADE)
    object = models.ForeignKey(Object, on_delete=models.CASCADE)
    completed_works = models.PositiveIntegerField()
    material = models.CharField(max_length=50)
    quantity_employee = models.PositiveIntegerField()
    date_start = models.DateTimeField()
    date_finish = models.DateTimeField()


class analytics_of_photo(models.Model):
    id = models.AutoField(primary_key=True)
    object = models.ForeignKey(Object, on_delete=models.CASCADE)
    number_of_violations = models.PositiveIntegerField()
















