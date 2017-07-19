# -*- coding: utf-8 -*-
 
#from django.http import HttpResponse
from django.shortcuts import render
 
def hello(request):
    context = {'hello':'Hello World!'} # 字典 context
    return render(request, 'hello.html', context)

