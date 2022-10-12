from urllib import request
from django.shortcuts import render
from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.

# Create your views here.
from logging import raiseExceptions
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View
# from matplotlib.style import available

from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from django.http import JsonResponse
import json
from .models import *
from rest_framework. exceptions import AuthenticationFailed
from rest_framework import status
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
from .utility import authentication_user
import jwt  ,datetime
from rest_framework.authentication import BasicAuthentication



class CustomerRegisterView(APIView):
    def post(self, request):
        payload, user, user_id = authentication_user(self,request, 'admin')
        request_data = request.data
        request_data['role'] = 'customer'
        serializer = CustomerSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data , status=status.HTTP_201_CREATED)

            

class AdminRegisterView(APIView):
    def post(self, request):
        request_data = request.data
        request_data['role'] = 'admin'
        serializer = CustomerSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data , status=status.HTTP_201_CREATED)
    

class AdminView(APIView):
    def get(self, request):
        payload, user, user_id = authentication_user(self,request, 'admin')

        # authentication_classes = [BasicAuthentication]
        # permission_classes = [IsAuthenticated]
        u = CustomUser.objects.all().values('username','phone')
        return Response(u)
    
    def patch(self , request):
        payload, user, user_id = authentication_user(self,request, 'admin')
        r  = request.data['username']
        print(r)
        p = request.data['new']
        print(p)
        u = list(CustomUser.objects.all().values_list('username'))
        print(u)
        for i in u:
            print(i)
            if i[0] == r:
                print(i)
                CustomUser.objects.filter(username=r).update(username=p)
                return Response('DONE')
        return Response('User not found')
    
    def post(self, request):
        payload, user, user_id = authentication_user(self,request, 'admin')




        # u = CustomUser.objects.all().values('phone')
            # print(i)

        # for t in u:
        #     if r == t:
        #         CustomUser.objects.update()

        return Response("hello")





class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = CustomUser.objects.filter(email=email).first()

        if user is None:
            # raise AuthenticationFailed('Credentials not found')
            return JsonResponse({"error":"Email Mismatch"}, status=401)
        
        if not user.check_password(password):
            # raise AuthenticationFailed('Incorrect Password')
            return JsonResponse({"error":"Incorrect passoword"}, status=401)
        
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=7200),
            'iat': datetime.datetime.utcnow()
        }
        token = jwt.encode(payload, 'secret',algorithm='HS256')
        


        response =  Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data= {
            'jwt' : token
        }

        return response




class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'Logged Out'
        }
        return response

class UserProfileView(APIView):

    def get(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated !')
        
        user = CustomUser.objects.filter(id=payload['id']).first()
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)
    


class Order(APIView):
    def post(self, request):
        payload, user, user_id = authentication_user(self,request, 'customer')
        request_data = request.data
        request_data['role'] = 'customer'
        serializer = CustomerSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data , status=status.HTTP_201_CREATED)

