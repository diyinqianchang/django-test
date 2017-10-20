from django.shortcuts import render
from django.http import *
from django.template import RequestContext,loader
from .models import *
from . import signals
from django.conf import settings
from django.core.paginator import Paginator
from django.views.decorators.cache import cache_page
from django.core.cache import cache
# Create your views here.



def index(request):

    booklist = BookInfo.objects.all()
    context = {'title':'学习','con':'hello','list':booklist}
    return render(request,'booktest/index.html',context=context)
    # temp = loader.get_template('booktest/index.html')
    # return HttpResponse(temp.render())

def bookshow(request,bid):
    book = BookInfo.objects.get(pk=bid)
    herolist = book.heroinfo_set.all()
    context = {'title': '学习', 'con': 'hello', 'book': book,'herolist':herolist}
    return render(request, 'booktest/show.html', context=context)

#路勁參數形式
def test(request,year,mon,day):

    b = BookInfo.books.get(pk=1)
    b.bread= 30
    b.save()

    return HttpResponse('year:%s,mon:%s,day:%s'%(year,mon,day))


def testget(request):
    # a = request.GET.get('a','ninide') #可以有個默認值
    # a = request.GET.getlist('a')        #一键多值
    signals.signalAllen.send(sender='signal',allen='test') #信号发动
    concrete_model = BookInfo._meta.concrete_model
    blist = BookInfo.books.values('btitle','bread')
    list1 = []
    for b in blist:
        list1.append(b)
        # for field in concrete_model._meta.local_fields:
        #     print(field.value_from_object(b))

    return JsonResponse({'list':list1})


def cookieTest(request):
    cookie = request.COOKIES
    response = HttpResponse()
    if 'ti' in cookie.keys():
        response.write(cookie['ti'])
    # resopnse.set_cookie('ti','abc')
    return response

def uploadPic(request):
    return render(request,'booktest/uploadPic.html')

def uploadHandle(request):

    if request.method == "POST":
        f = request.FILES['pic1']
        fname = '%s/%s'%(settings.MEDIA_ROOT,f.name)
        with open(fname,'wb') as pic:
            for c in f.chunks():
                pic.write(c)
        return HttpResponse(fname)
    else:
        return HttpResponse("error")


def pagetest(request,pindex='1'):

    list = HeroInfo.objects.all()
    paginator = Paginator(list,5)
    if pindex=='':
        pindex = '1'
    pindex = int(pindex)
    page = paginator.page(pindex)
    context = {'page':page}
    return render(request,'booktest/herolist.html',context=context)


# @cache_page(60)  #缓存一个视图
def cachel(request):
    cache.set('key1','value1',60)
    return render(request,'booktest/cache.html')
    # return HttpResponse('hello3')

def mysearch(request):
    return render(request,'booktest/mysearch.html')