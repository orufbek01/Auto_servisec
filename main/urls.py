from django.urls import path
from .views import *

urlpatterns = [
    path("get-employee/<slug:slug>/", get_employee),
    path("get-cassa/<slug:slug>/", get_cassa),
    path("get-order/<slug:slug>/", get_order),
    path("get-payment/<slug:slug>/", get_payment),
    path("get-report/<slug:slug>/", get_report),
    path("get_attendace/<slug:slug>/", get_attendace),

    path("employee_by_name/", employee_by_name),
    path("employee_by_phone_number/", employee_by_phone_number),
    path("employee_by_rating/", employee_by_rating),
    path("employee_age/", employee_age),
    path("employee_profession/", employee_profession),
    path("client_by_name/", client_by_name),
    path("client_by_phone_number/", client_by_phone_number),
    path("car_by_name/", car_by_name),
    path("order_by_is_deliveri/", order_by_is_deliveri),
    path("order_by_master/", order_by_master),
    path("fiter_order_by_dedline/", fiter_order_by_dedline),
    path("payment_by_code/", payment_by_code),
    path("payment_by_qr_code/", payment_by_qr_code),
    path("payment_by_date/", payment_by_date),
    path("report_by_datetime/", report_by_datetime),
    path("attendance_by_day/", attendance_by_day),
    path("attendance_by_employee_name/", attendance_by_employee_name),
    path("attendance_by_attend/", attendance_by_attend),
    path("attendance_by_attend/", attendance_by_attend),

    path("cassa_api/<slug:slug>/", cassa_api),
    path("employee_api/<slug:slug>/", employee_api),
    path("order_api/<slug:slug>/", order_api),
    path("payment_api/<slug:slug>/", payment_api),
]