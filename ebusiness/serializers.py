from rest_framework import serializers
from ebusiness.models import *

class EUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ebusiness_user
        fields = ('user_id','appname','keywords','status','create_time')

class EInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ebusiness_info
        fields = ('user_id','exist','stauts','website','title','href','author',
                  'description','content','create_time','publish_time','picurl',
                  'recommand_value','keyword')