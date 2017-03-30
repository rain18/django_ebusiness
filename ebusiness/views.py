from django.shortcuts import render
from ebusiness.serializers import *
from ebusiness.models import *
import django_filters.rest_framework

# Create your views here.
class EUserViewSet():
    queryset = ebusiness_user.objects.all()
    serializers = EUserSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = ('user_id', 'appname', 'keywords', 'status', 'create_time',)


class EInfoViewSet():
    queryset = ebusiness_info.objects.all()
    serializers = EInfoSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = ('user_id','exist','status','website','title','href','author',
                  'description','content','create_time','publish_time','picurl',
                  'recommand_value','keyword')