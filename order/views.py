from django.shortcuts import render

# Create your views here.
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
from orderplacementapi.utility import authentication_user
import jwt  ,datetime
from rest_framework.authentication import BasicAuthentication

from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser

class OrderView(APIView):

    parser_classes = (FileUploadParser,)
    parser_classes = (MultiPartParser, FormParser)


    def post(self, request):
        payload, user, user_id = authentication_user(self,request, 'customer')

        # parser_classes = (MultiPartParser, FormParser)

        file = request.data.get('file', None)
        print(user_id)
        if file:
            t = Order.objects.filter(customer_id=user_id).create(orderfile=file)
            return Response({"MSG":"DONE"})
        else:

        # serializer = OrderSerializer(data=request_data)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
            return Response({"msg":"failed"})
