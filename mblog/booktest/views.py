from django.shortcuts import render
from django.http import *
from django.template import RequestContext,loader
from .models import *

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