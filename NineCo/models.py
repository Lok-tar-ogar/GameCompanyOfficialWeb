# coding : utf-8
from django.db import models


class Carousel(models.Model):

    """docstring for Carousel"""
    Title = models.CharField('标题', max_length=50)
    Image = models.FileField('图片', upload_to='NineCo/static/img/')
    Linkto = models.CharField('链接地址（可为空）', max_length=50, blank=True)
    Caption = models.CharField('子标题', max_length=500, blank=True, null=True)
    dimDate = models.DateTimeField(auto_now_add=True)  # timezone.now()

    def __str__(self):
        return self.Title

    class Meta:
        verbose_name = '轮播管理'
        ordering = ['-dimDate']  # sorted news by dimdate


class ClassManger(models.Manager):

    def get_Class_list(self):  # get the job's class
        classf = Classification.objects.all()
        class_list = []
        for i in range(len(classf)):
            class_list.append([])
        for i in range(len(classf)):
            temp = Classification.objects.filter(name=class_list[i])
            posts = temp.JobsInfo_set.all()
            class_list[i].append(classf[i])
            class_list[i].append(len(posts))
        return class_list


class Classification(models.Model):  # job class
    name = models.CharField('分类名', max_length=25)

    objects = models.Manager()
    class_list = ClassManger()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '招聘类别'


class GameClass (models.Model):
    name = models.CharField('分类名', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '游戏类别'


class GameInfo(models.Model):
    name = models.CharField('游戏名', max_length=50)
    imgUrl = models.FileField('图片', upload_to='NineCo/static/img/')
    Url = models.CharField('下载地址', max_length=100, blank=True, null=True)
    content = models.TextField('详细介绍', max_length=4000, blank=True, null=True)
    gameType = models.ForeignKey(GameClass)
    dimDate = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '游戏信息'
        ordering = ['-dimDate']  # sorted news by dimdate


class JobsInfo(models.Model):
    jobTitle = models.CharField('职位名', max_length=50)  # job 's  name
    jobDetail = models.TextField('职位描述', max_length=2000)
    dimDate = models.DateTimeField(auto_now_add=True)  # timezone.now()
    classification = models.ForeignKey(Classification)
    status = models.CharField('职位状态', max_length=5)  # job's status

    def __str__(self):
        return self.jobTitle

    class Meta:
        verbose_name = '招聘信息'
        ordering = ['-dimDate']  # sorted news by dimdate


class News(models.Model):
    newsTitle = models.CharField('新闻标题', max_length=50)
    newsDetail = models.TextField('新闻详情', max_length=5000)
    # obviously it is what it looks like.
    viewedTimes = models.IntegerField('浏览次数')
    dimDate = models.DateTimeField(auto_now_add=True)  # timezone.now()

    def __str__(self):
        return self.newsTitle

    class Meta:
        verbose_name = '文章'
        ordering = ['-dimDate']  # sorted news by dimdate
