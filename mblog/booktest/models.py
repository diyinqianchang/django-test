from django.db import models

# Create your models here.


class BookInfoManager(models.Manager):
    def get_queryset(self):
        return super(BookInfoManager,self).get_queryset().filter(isDelete=False)


class BookInfo(models.Model):
    btitle = models.CharField(max_length=20,verbose_name='标题')
    bpub_date = models.DateTimeField(verbose_name='出版日期')
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(null=False)
    isDelete = models.BooleanField(default=False)
    # books1 = models.Manager()
    # books = BookInfoManager()
    class Meta:
        ordering = ['id']
        verbose_name = '武侠小说'
        verbose_name_plural='武侠小说'
    def __str__(self):
        return self.btitle

    @classmethod
    def create(cls,btitle,bpub_date):
        b = BookInfo()
        b.btitle = btitle
        b.bpub_date = bpub_date
        b.bread = 0
        b.bcomment = 0
        b.isDelete = False
        return b

class HeroInfo(models.Model):
    hname = models.CharField(max_length=10,verbose_name='名字')
    hgender = models.BooleanField(verbose_name='性别')
    hcontent = models.CharField(max_length=1000,verbose_name='内容简介')
    hbook = models.ForeignKey(BookInfo,verbose_name='书')
    isDelete = models.BooleanField(default=False)

    class Meta:
        ordering=['hbook']
        verbose_name = '英雄'
        verbose_name_plural = '英雄'
    def __str__(self):
        return self.hname
