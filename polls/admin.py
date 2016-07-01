# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Question
from .models import Choice
# Register your models here.
class ChoiceInline(admin.TabularInline):
	#使用 TabularInline（不是StackedInline）
	#这些相关联的对象显示成紧凑的、基于表格的形式
    model = Choice
    extra = 3
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    #自定义的方法was_published_recently
    list_filter = ['pub_date']
    #对字段进行过滤
    search_fields = ['question_text']
    #搜索功能
admin.site.register(Question,QuestionAdmin)
#admin.site.register(Choice)
#告诉管理站点Question 对象要有一个管理界面
