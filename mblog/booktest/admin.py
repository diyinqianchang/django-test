from django.contrib import admin

# Register your models here.

from .models import *


#关联对象
class HeroInfoInline(admin.TabularInline):
    model = HeroInfo
    extra = 3

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id','btitle','bpub_date']
    list_filter = ['btitle']    #列表过滤
    search_fields = ['btitle']  #以什么字段搜索
    list_per_page = 10
    fieldsets = [
        ('base',{'fields':['btitle']}),
        ('super',{'fields':['bpub_date']})
    ]

    inlines = [HeroInfoInline]

admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo)