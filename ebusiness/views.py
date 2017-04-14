from django.shortcuts import render
from ebusiness.serializers import *
from ebusiness.models import *
import django_filters.rest_framework
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from django.middleware.csrf import CsrfViewMiddleware

# Create your views here.
# @csrf_exempt
class EUserViewSet(viewsets.ModelViewSet):
    queryset = ebusiness_user.objects.all()
    serializer_class = EUserSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = ('user_id', 'appname', 'keywords', 'status', 'create_time',)

# @csrf_exempt
class EInfoViewSet(viewsets.ModelViewSet):
    queryset = ebusiness_info.objects.all()
    serializer_class = EInfoSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = ('user_id','exist','status','website','title','href','author',
                  'description','content','create_time','publish_time','picurl',
                  'recommand_value','keyword')