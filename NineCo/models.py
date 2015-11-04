# coding : utf-8
from django.db import models


class UserAdmin(models.Model):
    userName = models.CharField(max_length=50)
    userPsd = models.CharField(max_length=50)
    regDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.userName


class Carousel(models.Model):

    """docstring for Carousel"""
    Title = models.CharField(max_length=50)
    Image = models.CharField(max_length=50)
    Linkto = models.CharField(max_length=50)
    Caption = models.CharField(max_length=500, blank=True, null=True)
    dimDate = models.DateTimeField(auto_now_add=True)  # timezone.now()

    def __str__(self):
        return self.Title


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
    name = models.CharField(max_length=25)

    objects = models.Manager()
    class_list = ClassManger()

    def __str__(self):
        return self.name


class GameClass (models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class GameInfo(models.Model):
    name = models.CharField(max_length=50)
    imgUrl = models.CharField(max_length=50, blank=True)
    Url = models.CharField(max_length=100, blank=True, null=True)
    content = models.CharField(max_length=4000, blank=True, null=True)
    gameType = models.ForeignKey(GameClass)
    dimDate = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class JobsInfo(models.Model):
    jobTitle = models.CharField(max_length=50)  # job 's  name
    jobDetail = models.CharField(max_length=2000)
    dimDate = models.DateTimeField(auto_now_add=True)  # timezone.now()
    classification = models.ForeignKey(Classification)
    status = models.CharField(max_length=5)  # job's status

    def __str__(self):
        return self.jobTitle


class News(models.Model):
    newsTitle = models.CharField(max_length=50)
    newsDetail = models.TextField(max_length=5000)
    viewedTimes = models.IntegerField()  # obviously it is what it looks like.
    dimDate = models.DateTimeField(auto_now_add=True)  # timezone.now()

    def __str__(self):
        return self.newsTitle

    class Meta:
        ordering = ['-dimDate']  # sorted news by dimdate
