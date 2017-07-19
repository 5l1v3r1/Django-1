# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
from django.db import models

#修改models.py 后要建表 
# $ python manage.py makemigrations TestModel   模型有变更
# $ python manage.py migrate TestModel   创建表结构

# 可通过admin.py管理工具管理模型
# Test 模型，类名 Test 为数据库表名，且继承了models.Model,Django会自动添加一个id作为主键
class Test(models.Model):
    name = models.CharField(max_length=20) # 数据表中的字段 name，char length

# Contact 模型 
class Contact(models.Model):
    name   = models.CharField(max_length=200)
    age    = models.IntegerField(default=0)
    email  = models.EmailField()
    def __unicode__(self):
        return self.name

# Tag 模型 
class Tag(models.Model):
    #Tag 以 Contact 为外部键，一个 Contact 可以对应多个 Tag。
    contact = models.ForeignKey(Contact)
    name    = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name
