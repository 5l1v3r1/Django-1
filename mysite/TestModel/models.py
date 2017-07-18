# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
from django.db import models

#修改models.py 后要建表 
# $ python manage.py makemigrations TestModel   模型有变更
# $ python manage.py migrate TestModel   创建表结构
# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=20)
 
class Contact(models.Model):
    name   = models.CharField(max_length=200)
    age    = models.IntegerField(default=0)
    email  = models.EmailField()
    def __unicode__(self):
        return self.name
 
class Tag(models.Model):
    contact = models.ForeignKey(Contact)
    name    = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name
