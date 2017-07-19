# -*- coding: UTF-8 -*-

from django.conf.urls import url
from django.contrib import admin
from . import view,testdb,search,search2
 
urlpatterns = [
    # url(regex:正则,view:与正则匹配的 URL 请求,kwargs:字典类型参数,name:反向获取 URL)
    # 激活管理工具 admin
    url(r'^admin/', admin.site.urls),
    # 绑定 URL 与视图函数 hello
    url(r'^hello$', view.hello),# view.py 中的 hello
    url(r'^testdb$', testdb.testdb),
    url(r'^search-form$', search.search_form),
    url(r'^search$', search.search),
    url(r'^search-post$', search2.search_post),
]
