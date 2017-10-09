from django.db import models

# Create your models here.


class BookInfo(models.Model):
    btitle = models.CharField(max_length=20,verbose_name='标题')
    bpub_date = models.DateTimeField(verbose_name='出版日期')
    def __str__(self):
        return self.btitle

class HeroInfo(models.Model):
    hname = models.CharField(max_length=10,verbose_name='名字')
    hgender = models.BooleanField(verbose_name='性别')
    hcontent = models.CharField(max_length=1000,verbose_name='内容简介')
    hbook = models.ForeignKey(BookInfo,verbose_name='书')

    def __str__(self):
        return self.hname