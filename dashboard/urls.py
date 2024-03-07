from django.urls import path
from . import views

urlpatterns = [
    path("create-employee/",views.CreateEmployee.as_view()),
    path("update-employee/<int:pk>/",views.UpdateEmployee.as_view()),
    path("delete-employee/<int:pk>/",views.DeleteEmployee.as_view()),

    path('create-payment/', views.CreatePayment.as_view()),
    path('update-payment/<int:pk>/', views.UpdatePayment.as_view()),
    path('delete-payment/<int:pk>/', views.DeletePayment.as_view()),

    path('create-attendace/', views.CreateAttendace.as_view()),
    path('update-attendace/<int:pk>/', views.UpdateAttendace.as_view()),
    path('delete-attendace/<int:pk>/', views.DeleteAttendace.as_view()),

    path('create-cassa/', views.CreateCassa.as_view()),
    path('update-cassa/<int:pk>/', views.UpdateCassa.as_view()),
    path('delete-cassa/<int:pk>/', views.DeleteCassa.as_view()),

    path('create-order/', views.CreateOrder.as_view()),
    path('update-order/<int:pk>/', views.UpdateOrder.as_view()),
    path('delete-order/<int:pk>/', views.DeleteOrder.as_view()),

    path('create-report/', views.CreateReport.as_view()),
    path('update-report/<int:pk>/', views.UpdateReport.as_view()),
    path('delete-report/<int:pk>/', views.DeleteReport.as_view()),
]