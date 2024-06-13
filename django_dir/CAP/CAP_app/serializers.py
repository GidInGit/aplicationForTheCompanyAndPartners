from rest_framework import serializers


class CompanySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()

class ObjectSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    address = serializers.CharField()
    start_time = serializers.DateTimeField()
    end_time = serializers.DateTimeField()

class EmployeeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    full_name = serializers.CharField()
    role =serializers.CharField()
    object_name = serializers.CharField(source='object.name', read_only=True)
    foreman_full_name = serializers.CharField(source='foreman.full_name', read_only=True)
    bracelet_rfid = serializers.CharField(source= 'bracelet.rfid', read_only=True)

class ForemanSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    full_name = serializers.CharField()
    role =serializers.CharField()
    object_name = serializers.CharField(source='object.name', read_only=True)
    bracelet_rfid = serializers.CharField(source= 'bracelet.rfid', read_only=True)

class BraceletSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    rfid = serializers.CharField()
    in_use = serializers.BooleanField()

class ChipSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    chip_number = serializers.CharField()
    in_use = serializers.BooleanField()

