from .models import *
from . import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.template.defaultfilters import slugify


@api_view(["GET"])
def get_employee(request, slug):
    employee = Employee.objects.get(slug = slug)
    ser = serializers.EmployeeSerializer(employee)
    return Response(ser.data)


@api_view(["GET"])
def get_cassa(request, slug):
    cassa = Cassa.objects.get(slug = slug)
    ser = serializers.CassaSerializer(cassa)
    return Response(ser.data)


@api_view(["GET"])
def get_order(request, slug):
    order = Order.objects.get(slug = slug)
    ser = serializers.OrderSerializer(order)
    return Response(ser.data)


@api_view(["GET"])
def get_payment(request, slug):
    payment = Paymet.objects.get(slug = slug)
    ser = serializers.PaymetSerializer(payment)
    return Response(ser.data)

@api_view(["GET"])
def get_report(request, slug):
    report = Report.objects.get(slug = slug)
    ser = serializers.ReportSerializer(report)
    return Response(ser.data)


@api_view(["GET"])
def get_attendace(request, slug):
    attendace = Attends.objects.get(slug = slug)
    ser = serializers.AttendanceSerializer(attendace)
    return Response(ser.data)


""" Start Filter """

@api_view(["GET"])
def employee_by_name(request):
    name = request.GET.get("name")
    employee = Employee.objects.filter(name = name)
    ser = serializers.EmployeeSerializer(employee)
    return Response(ser.data)


@api_view(["GET"])
def employee_by_phone_number(request):
    phone_number = request.GET.get("phone_number")
    employee = Employee.objects.filter(phone_number = phone_number)
    ser = serializers.EmployeeSerializer(employee)
    return Response(ser.data)


@api_view(["GET"])
def employee_by_rating(request):
    rating = request.GET.get("rating")
    employee = Employee.objects.filter(rating = rating)
    ser = serializers.EmployeeSerializer(employee)
    return Response(ser.data)


@api_view(["GET"])
def employee_age(request):
    age = request.GET.get("age")
    employee = Employee.objects.filter(age = age)
    ser = serializers.EmployeeSerializer(employee)
    return Response(ser.data)


@api_view(["GET"])
def employee_profession(request):
    profession = request.GET.get("profession")
    employee = Employee.objects.filter(profession = profession)
    ser = serializers.EmployeeSerializer(employee)
    return Response(ser.data)


@api_view(["GET"])
def client_by_name(request):
    name = request.GET.get("name")
    order = Order.objects.filter(name = name)
    ser = serializers.OrderSerializer(order)
    return Response(ser.data)


@api_view(["GET"])
def client_by_phone_number(request):
    phone_number = request.GET.get("phone_number")
    order = Order.objects.filter(phone_number = phone_number)
    ser = serializers.OrderSerializer(order)
    return Response(ser.data)


@api_view(["GET"])
def car_by_name(request):
    name = request.GET.get("name")
    car = Order.objects.filter(name = name)
    ser = serializers.OrderSerializer(car)
    return Response(ser.data)


@api_view(["GET"])
def order_by_is_deliveri(request):
    is_deliveri = request.GET.get("is_delivery")
    order = Order.objects.filter(is_deliveri = is_deliveri)
    ser = serializers.OrderSerializer(order)
    return Response(ser.data)


@api_view(["GET"])
def order_by_master(request):
    master = request.GET.get("master")
    oOrder.objects.filter(master = master)
    ser = serializers.OrderSerializer(order)
    return Response(ser.data)


@api_view(['GET'])
def fiter_order_by_dedline(request):
    dedline = request.GET['dedline']
    day = str(dedline)[8:10]
    order = Order.objects.filter(is_active=True)
    filter_order = []
    for i in order:
        if str(i.dedline)[8:10] == day:
            filter_order.append(i)
    ser = OrderSerializer(filter_order, many=True)
    return Response(ser.data)



@api_view(["GET"])
def payment_by_code(request):
    code = request.GET.get("code")
    payment = Paymet.objeects.filter(code = code)
    ser = serializers.PaymentSerializer(code)
    return Response(ser.data)


@api_view(["GET"])
def payment_by_qr_code(request):
    qr_code = request.GET.get("qr_code")
    payment = Paymet.objects.filter(qr_code = qr_code)
    ser = serializers.PaymentSerializer(payment)
    return Response(ser.data)


@api_view(["GET"])
def payment_by_date(request):
    date = request.GET.get("date")
    payPaymet.objects.filter(date = date)
    ser = serializers.PaymentSerializer(payment)
    return Response(ser.data)


@api_view(["GET"])
def report_by_datetime(request):
    start_time = request.GET.get("s_time")
    end_time = request.GET.get("e_time")
    reReport.objects.filter(time__gte = start_time, time__lte = end_time)
    ser = serializers.ReportSerializer(report)
    return Response(ser.data)


@api_view(["GET"])
def attendance_by_day(request):
    day = request.GET.get("day")
    attendence = Attends.objects.filter(day = day)
    ser = serializers.AttendanceSerializer(attendence)
    return Response(ser.data)


@api_view(["GET"])
def attendance_by_employee_name(request):
    name = request.GET.get("name")
    attendace = Attends.objects.filter(name = name)
    ser = serializers.AttendanceSerializer(attendace)
    return Response(ser.data)


@api_view(["GET"])
def attendance_by_attend(request):
    attend = request.GET.get("attend")
    attenAttends.objects.filter(attend = attend)
    ser = serializers.AttendanceSerializer(attendace)
    return Response(ser.data)

""" End Filter """

""" Start get pk """

@api_view(["GET"])
def cassa_api(request, slug):
    cassa =Cassa.objects.get(slug = 1)
    ser = serializers.CassaSerializer(cassa)
    return Response(ser.data)


@api_view(["GET"])
def employee_api(request, slug):
    employee = Employee.objects.get(slug = slug)
    ser = serializers.EmployeeSerializer(employee, many=True)
    return Response(ser.data)


@api_view(["GET"])
def order_api(request, slug):
    order = Order.objects.get(slug = slug)
    ser = serializers.OrderSerializer(order)
    return Response(ser.data)


@api_view(["GET"])
def payment_api(request, slug):
    payment = Paymet.objects.get(slug = slug)
    ser = serializers.PaymentSerializer(payment)
    return Response(ser.data)
