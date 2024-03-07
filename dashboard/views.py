from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,UpdateAPIView,DestroyAPIView
from main import models
from main import serializers

# ---------- Start Employee CRUD -------------

class CreateEmployee(ListCreateAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer


class UpdateEmployee(UpdateAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer


class DeleteEmployee(DestroyAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer

#  -------------- End Employee CRUD ----------------

# -------------- Start Cassa Crud ------------------

class CreateCassa(ListCreateAPIView):
    queryset = models.Cassa.objects.all()
    serializer_class = serializers.CassaSerializer


class UpdateCassa(UpdateAPIView):
    queryset = models.Cassa.objects.all()
    serializer_class = serializers.CassaSerializer


class DeleteCassa(DestroyAPIView):
    queryset = models.Cassa.objects.all()
    serializer_class = serializers.CassaSerializer

# ----------------- END Cassa CRUD -------------------

# ----------------- Start Order CRUD ------------------

class CreateOrder(ListCreateAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer


class UpdateOrder(UpdateAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer


class DeleteOrder(DestroyAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer

# ----------------- End Order CRUD ------------------

# ---------------- Start Payment CRUD --------------

class CreatePayment(ListCreateAPIView):
    queryset = models.Paymet.objects.all()
    serializer_class = serializers.PaymentSerializer


class UpdatePayment(UpdateAPIView):
    queryset = models.Paymet.objects.all()
    serializer_class = serializers.PaymentSerializer


class DeletePayment(DestroyAPIView):
    queryset = models.Paymet.objects.all()
    serializer_class = serializers.PaymentSerializer

# --------------- End Payment CRUD -----------------

# -------------- Start Report CRUD -----------------

class CreateReport(ListCreateAPIView):
    queryset = models.Report.objects.all()
    serializer_class = serializers.ReportSerializer


class UpdateReport(UpdateAPIView):
    queryset = models.Report.objects.all()
    serializer_class = serializers.ReportSerializer


class DeleteReport(DestroyAPIView):
    queryset = models.Report.objects.all()
    serializer_class = serializers.ReportSerializer

# --------------- End Report CRUD ----------------

# --------------- Start Attendece CRUD -----------

class CreateAttendace(ListCreateAPIView):
    queryset = models.Attends.objects.all()
    serializer_class = serializers.AttendanceSerializer


class UpdateAttendace(UpdateAPIView):
    queryset = models.Attends.objects.all()
    serializer_class = serializers.AttendanceSerializer


class DeleteAttendace(DestroyAPIView):
    queryset = models.Attends.objects.all()
    serializer_class = serializers.AttendanceSerializer

# ----------------- End Attendace CRUD -------------