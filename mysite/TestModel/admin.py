# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from TestModel.models import Test,Contact,Tag
 
#  models.py 中 Contact 是 Tag 的外部键
#  通过内联 (Inline) 让 Tag 附加在 Contact 的编辑页面上显示。
#  用 admin.TabularInline 会显示成紧凑的、基于表格的形式
class TagInline(admin.TabularInline):
    model = Tag
    extra = 1 # 提供1个Tag空间。默认提供3个

# 自定义管理页面 定义一个 ContactAdmin 类
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','age', 'email') # 通过list_display 属性定义显示的栏目
    list_filter = ['age'] # 添加过滤器，通过 age 变更进行过滤
    search_fields = ('name',) # 添加搜索栏，根据 name 子段搜索
    inlines = [TagInline]  # Inline
     # 将输入栏分为Main 和 Advance 两部分
    fieldsets = (
        ['Main',{
            'fields':('name','email'),# fields 属性定义了要显示的字段
        }],
        ['Advance',{
            'classes': ('collapse',),#classes 说明它所在的部分的 CSS 格式，这里让 Advance 部分隐藏
            'fields': ('age',),
        }]
 
    )

# ContactAdmin 类,对应 Contact 数据模型
admin.site.register(Contact, ContactAdmin)
# 注册模型并显示，通过 admin.py 管理
admin.site.register([Test])
