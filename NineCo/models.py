# coding : utf-8
from django.db import models


class Carousel(models.Model):

    """docstring for Carousel"""
    Title = models.CharField('标题', max_length=50)
    Image = models.FileField('图片（1920*500）', upload_to='img/')
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
    imgUrl = models.FileField('主要图片（120*120）', upload_to='img/')
    Url = models.FileField(
        '上传APP',  blank=True, null=True, upload_to='apps/')
    QRimg = models.FileField(
        '上传二维码图片（120*120）',  blank=True, null=True, upload_to='img/')
    content = models.TextField('详细介绍', max_length=4000, blank=True, null=True)
    version = models.CharField('游戏版本', max_length=50, blank=True, default='#')
    gamesize = models.CharField(
        '游戏大小', max_length=50, blank=True, default='30MB')
    imgContent1 = models.FileField(
        '图片介绍1（296*524）', blank=True, null=True, upload_to='img/')
    imgContent2 = models.FileField(
        '图片介绍2（同上）', blank=True, null=True, upload_to='img/')
    imgContent3 = models.FileField(
        '图片介绍3', blank=True, null=True, upload_to='img/')
    imgShow = models.FileField(
        '游戏中心展示（用于展示在首页和游戏列表的图）', blank=True, null=True, upload_to='img/')
    gameType = models.ForeignKey(GameClass)
    forumLink = models.CharField('论坛链接', blank=True, null=True, max_length=50)
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
    upLoadImg = models.FileField(
        '上传新闻中的图片，引用图片请采用"/static/img/xxx.xx"格式', blank=True, null=True, upload_to='img/')
    viewedTimes = models.IntegerField('浏览次数')
    dimDate = models.DateTimeField(auto_now_add=True)  # timezone.now()

    def __str__(self):
        return self.newsTitle

    class Meta:
        verbose_name = '业务咨询'
        ordering = ['-dimDate']  # sorted news by dimdate


class NewsOfBus(models.Model):
    newsTitle = models.CharField('业务标题', max_length=50)
    newsDetail = models.TextField('业务详情', max_length=5000)
    # obviously it is what it looks like.
    imgShow = models.FileField(
        '展示业务咨询页面的图片', blank=True, null=True, upload_to='img/')

    upLoadImg = models.FileField(
        '上传新闻中的图片，引用图片请采用"/static/img/xxx.xx"格式', blank=True, null=True, upload_to='img/')
    viewedTimes = models.IntegerField('浏览次数')
    dimDate = models.DateTimeField(auto_now_add=True)  # timezone.now()

    def __str__(self):
        return self.newsTitle

    class Meta:
        verbose_name = '文章'
        ordering = ['-dimDate']  # sorted news by dimdate
