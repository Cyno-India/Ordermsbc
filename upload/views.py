from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from orderplacementapi.models import CustomUser
from orderplacementapi.utility import authentication_user
# Create your views here.
from rest_framework import viewsets, parsers
from .models import Docs
from .serializers import DropBoxSerializer
from rest_framework.response import Response

class DropBoxViewset(APIView):
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]

    def post(self, request, *args, **kwargs):
        payload, user, user_id = authentication_user(self,request, 'customer')
        request.data['customer_id'] = user_id
        user_instance = CustomUser.objects.filter(id=user_id)
        if request.method == "POST":
            allimages = request.FILES['file']
            t = Docs.objects.filter(customer_id=user_id).create(customer_id=user_instance[0],document=allimages)
            return Response('hello')


# queryset = Drop.objects.all()
# serializer_class = DropBoxSerializer
# parser_classes = [parsers.MultiPartParser, parsers.FormParser]
# http_method_names = ['get', 'post', 'patch', 'delete']