from django.db import models

# Create your models here.


class UserAdmin(models.Model):
    userName = models.CharField(max_length=50)
    userPsd = models.CharField(max_length=50)
    regDate = models.DateTimeField(blank=True)

    def __str__(self):
        return self.userName


class Carousel(models.Model):

    """docstring for Carousel"""
    Title = models.CharField(max_length=50)
    Image = models.CharField(max_length=50)
    Linkto = models.CharField(max_length=50)
    Caption = models.CharField(max_length=500, blank=True)
    dimDate = models.DateTimeField()  # timezone.now()

    def __str__(self):
        return self.Title


class JobsInfo(models.Model):
    jobTitle = models.CharField(max_length=50)
    # jobFrom=models.ForeignKey(JobsSort)
    jobDetail = models.CharField(max_length=2000)
    dimDate = models.DateTimeField()  # timezone.now()

    def __str__(self):
        return self.jobTitle


class JobsSort(models.Model):
    sortName = models.CharField(max_length=50)
    sortFather = models.ForeignKey(JobsSort, blank=True)
    jobTo = models.ForeignKey(JobsInfo, blank=True)
    dimDate = models.DateTimeField()  # timezone.now()

    def __str__(self):
        return self.sortName


class News(models.Model):
    newsTitle = models.CharField(max_length=50)
    newsDetail = models.CharField(max_length=5000)
    viewedTimes = models.IntegerField()  # obviously it is what it looks like.
    dimDate = models.DateTimeField()  # timezone.now()

    def __str__(self):
        return self.sortName
