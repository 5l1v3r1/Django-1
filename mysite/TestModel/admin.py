# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from TestModel.models import Test,Contact,Tag
 
#  models.py 中 Contact 是 Tag 的外部键
#  通过内联 (Inline) 让 Tag 附加在 Contact 的编辑页面上显示。
class TagInline(admin.TabularInline):
    model = Tag

# 自定义管理页面 定义一个 ContactAdmin 类
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','age', 'email') # 通过list_display 属性定义显示的栏目
    search_fields = ('name',) # 添加搜索栏
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
