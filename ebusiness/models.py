from django.db import models
import uuid

# Create your models here.
class ebusiness_user(models.Model):
    user_id = models.CharField(max_length=32,primary_key=True)
    appname = models.CharField(max_length=32)
    keywords = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    create_time = models.DateTimeField(auto_now=True)

#电商爬取信息的表
class ebusiness_info(models.Model):
    exist_type=(
        ('EXIST_ACTIVE','EXIST_ACTIVE'),
        ('EXIST_DELETE','EXIST_DELETE'),
    )
    status_type=(
        ('STATUS_DRAFT','STATUS_DRAFT'),
        ('STATUS_CHECKING','STATUS_CHECKING'),
        ('STATUS_ONLINE','STATUS_ONLINE'),
    )
    user_id = models.CharField(max_length=32)
    exist = models.TextField(choices=exist_type)
    status = models.TextField(choices=status_type)
    website = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    href = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    description = models.CharField(max_length=2048)
    content = models.CharField(max_length=15000)
    create_time = models.DateTimeField(auto_now=True)
    publish_time = models.DateTimeField()
    picurl = models.CharField(max_length=256,default='http://freedisk.free4inno.com/download?uuid=30d36e6a-613b-4ef9-87c3-c83020dc7049')
    recommand_value = models.IntegerField(default=0)
    keyword = models.CharField(max_length=32)