from django.shortcuts import render
from rest_framework.generics import UpdateAPIView
import main.serializers
from main.models import User
from main.serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth import login, authenticate, logout
from rest_framework.permissions import IsAuthenticated
from .token import get_tokens_for_user

""" Start accaunt view """
@api_view(['POST'])
def signin_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    try:
        usr = authenticate(username=username, password=password)
        try:
            if usr is not None:
                login(request, usr)
                tokens = get_tokens_for_user(usr)
                status = 200
                data = {
                    'status': status,
                    'username': username,
                    'token': tokens,
                }
            else:
                status = 403
                message = "Invalid Password or Username!"
                data = {
                    'status': status,
                    'message': message,
                }
        except User.DoesNotExist:
            status = 404
            message = 'This User is not defined! '
            data = {
                'status': status,
                'message': message,
            }
        return Response(data)
    except Exception as err:
        return Response(f'{err}')


@api_view(['POST'])
def singup_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    phone_number = request.POST.get('phone_number')
    new = User.objects.create_user(
        username = username,
        password = password,
        phone_number = phone_number
    )
    ser = UserSerializer(new)
    return Response(ser.data)


class UpdateUser(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = main.serializers.UserSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def logoout(request):
    logout(request)
    return Response({'data':'sucses'})

""" End accound view """