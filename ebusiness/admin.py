from django.contrib import admin
from ebusiness.models import *

# Register your models here.
class EUserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'appname', 'keywords',
                    'status', 'create_time',)
    search_fields = ('user_id', 'appname', 'keywords',
                     'status', 'create_time',)


class EInfoAdmin(admin.ModelAdmin):
    list_display = ('user_id','exist','status','website','title','href','author',
                  'description','content','create_time','publish_time','picurl',
                  'recommand_value','keyword')
    search_fields = ('user_id','exist','status','website','title','href','author',
                  'description','content','create_time','publish_time','picurl',
                  'recommand_value','keyword')


admin.site.register(ebusiness_user, EUserAdmin)
admin.site.register(ebusiness_info, EInfoAdmin)