#coding:UTF-8from django.conf.urls import urlfrom .views import *urlpatterns=[    url(r'^as/$',index),    url(r'^as/book/(\d+)$',bookshow)]