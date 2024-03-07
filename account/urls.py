from django.urls import path
from .views import *

urlpatterns = [
    path('sign', signin_view ),
    path('signup', singup_view )
