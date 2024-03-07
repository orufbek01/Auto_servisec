from . import models
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = models.Employee
        fields = "__all__"


class CassaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cassa
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = models.Order
        fields = "__all__"


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 3
        model = models.Paymet
        fields = "__all__"


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Report
        fields = "__all__"


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = models.Attends
        fields = "__all__"