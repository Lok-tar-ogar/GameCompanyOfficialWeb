from django.shortcuts import render
from django.shortcuts import render_to_response
from NineCo.models import JobsInfo, Classification, Carousel, GameInfo, GameClass, News ,NewsOfBus,NewsImg
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
import base64
from pyDes import *
import urllib.parse
import urllib
import sys
import http.cookiejar
import json




def Index(request):
    # url = "http://123.59.24.94:8093/login"
    # postdata = urllib.parse.urlencode({'userName': '123', 'pwd': '123'})
    # postdata = postdata.encode('utf-8')
    # f = urllib.request.urlopen(url,postdata)
    # games = GameInfo.objects.all().order_by('-dimDate')[0:6]
    # for i in range(0, len(games)):
    #     games[i].content = games[i].content[0:20]
    # carousel = Carousel.objects.all()[::-1]
    # gamelist = GameInfo.objects.all()[0:3]
    #
    # news = News.objects.all()[0:7]
    # new1=news[0]
    # news=news[1:7]
    # newsimg=NewsImg.objects.all()[0]
    return render(request, "index.html", locals())


def summary(request):
    return render(request, "summary.html")


def contact(request):
    return render(request, "contact.html")


def jobs(request):
    jobsinfos = JobsInfo.objects.all().order_by('-dimDate')
    classifications = Classification.objects.all()
    return render(request, "jobs.html", {'jb': jobsinfos, 'cl': classifications})


def gamelist(request):
    games = GameInfo.objects.all().order_by('-dimDate')
    return render(request, "gamelist.html", {'gm': games})


def gamecl(request):
    games = GameInfo.objects.all().order_by('-dimDate')
    gc = GameClass.objects.all()
    return render(request, "allgame.html", {'gm': games, 'gc': gc})


PageCount = 8
PAGERLEN = 8


def NewsPage(request):
    try:
        curpage = int(request.GET.get('curpage', '1'))
        allpage = int(request.GET.get('allpage', '1'))
        pagetype = str(request.GET.get('pagetype', ''))
    except ValueError:
        curpage = 1
        allpage = 1
        pagetype = 1
    if pagetype == 'pagedown':
        curpage += 1
    elif pagetype == 'pageup':
        curpage -= 1
    elif pagetype == 'pageto':
        pass
    startpos = (curpage - 1) * PageCount
    endpos = startpos + PageCount
    posts = News.objects.all().order_by('-dimDate')[startpos:endpos]
    if curpage == 1 and allpage == 1:
        allNewsCount = News.objects.count()
        allpage = allNewsCount // PageCount
        remainPost = allNewsCount % PageCount
        if remainPost > 0:
            allpage += 1
    pagelist = []  # below are the logic of pagination
    if(allpage - curpage > PAGERLEN - 2):
        for i in range(curpage - 1 - PAGERLEN // 2 if curpage - 1 - PAGERLEN // 2 > 0 else 0, curpage - 1 + PAGERLEN // 2):
            pagelist.append(i + 1)
            if len(pagelist) > PAGERLEN - 1:
                break
    else:
        if (curpage - 1 - PAGERLEN // 2 > 0):
            for i in range(curpage - 1 - PAGERLEN // 2, curpage - 1 + PAGERLEN // 2 if curpage - 1 + PAGERLEN // 2 < allpage else allpage):
                pagelist.append(i + 1)
                if len(pagelist) > PAGERLEN - 1:
                    break
        else:
            for i in range(0, curpage - 1 + PAGERLEN // 2 if curpage - 1 + PAGERLEN // 2 < allpage else allpage):
                pagelist.append(i + 1)
                if len(pagelist) > PAGERLEN - 1:
                    break

    return render(request, 'News.html', {'news': posts, 'allpage': allpage, 'borderpage': allpage - 3, 'pagelist': pagelist, 'curpage': curpage})


def gamed(request, i):
    game = GameInfo.objects.get(id=i)
    return render(request, 'showgame.html', {'game': game})


def NewsDetail(request, newsid):
    news = News.objects.get(id=newsid)
    return render(request, 'NewsDetail.html', locals())
def sign(s):#签名加密方式
    k = des("MV03ND.f", ECB, "\0\0\0\0\0\0\0\0",
                pad=None, padmode=PAD_PKCS5)
    return base64.b64encode(k.encrypt(s))
def post(url, data):#封装post方法
    return urllib.request.urlopen(url, urllib.parse.urlencode(data).encode('utf-8')).read()

def login(request):
    if request.method == "POST":
        uf = request.POST
        username = uf.get('username')
        pwd = uf.get('pwd')
        d=sign(username+pwd)
        data = {'userName': username, 'pwd': pwd, 'sign': d}
        callbackData = {}#返回数据        
        callbackData = json.loads(
            str(post('http://123.59.24.94:8093/login', data), encoding="utf-8"))
        if(callbackData['code'] == 1):
            request.session['username'] = username
            return HttpResponseRedirect('/')
        else:

            return render(request, 'login.html',{'info':'1'})

    else:
        if('username' not in request.session):
            return render(request, 'login.html')
        else:
            return HttpResponseRedirect('/')


def logout(request):
    del request.session['username']
    return HttpResponseRedirect('/')


def regist(request):
    
    return render(request, 'regist.html')

BPageCount = 3
BPAGERLEN = 8

def NewsOfB(request):
    try:
        curpage = int(request.GET.get('curpage', '1'))
        allpage = int(request.GET.get('allpage', '1'))
        pagetype = str(request.GET.get('pagetype', ''))
    except ValueError:
        curpage = 1
        allpage = 1
        pagetype = 1
    if pagetype == 'pagedown':
        curpage += 1
    elif pagetype == 'pageup':
        curpage -= 1
    elif pagetype == 'pageto':
        pass
    startpos = (curpage - 1) * BPageCount
    endpos = startpos + BPageCount
    bnews = NewsOfBus.objects.all()[startpos:endpos]
    if curpage == 1 and allpage == 1:
        allNewsCount = NewsOfBus.objects.count()
        allpage = allNewsCount // BPageCount
        remainPost = allNewsCount % BPageCount
        if remainPost > 0:
            allpage += 1
    pagelist = []  # below are the logic of pagination
    if(allpage - curpage > BPAGERLEN - 2):
        for i in range(curpage - 1 - BPAGERLEN // 2 if curpage - 1 - BPAGERLEN // 2 > 0 else 0, curpage - 1 + BPAGERLEN // 2):
            pagelist.append(i + 1)
            if len(pagelist) > BPAGERLEN - 1:
                break
    else:
        if (curpage - 1 - BPAGERLEN // 2 > 0):
            for i in range(curpage - 1 - BPAGERLEN // 2, curpage - 1 + BPAGERLEN // 2 if curpage - 1 + BPAGERLEN // 2 < allpage else allpage):
                pagelist.append(i + 1)
                if len(pagelist) > BPAGERLEN - 1:
                    break
        else:
            for i in range(0, curpage - 1 + BPAGERLEN // 2 if curpage - 1 + BPAGERLEN // 2 < allpage else allpage):
                pagelist.append(i + 1)
                if len(pagelist) > BPAGERLEN - 1:
                    break

    return render(request,'bussinessWeb.html',{'bnews': bnews, 'allpage': allpage, 'borderpage': allpage - 3, 'pagelist': pagelist, 'curpage': curpage})

GPageCount = 9
GPAGERLEN = 8
def gameCenter(request):
    game = GameInfo.objects.all().order_by('-dimDate')
    gc = GameClass.objects.all()
    try:
        curpage = int(request.GET.get('curpage', '1'))
        allpage = int(request.GET.get('allpage', '1'))
        pagetype = str(request.GET.get('pagetype', ''))
    except ValueError:
        curpage = 1
        allpage = 1
        pagetype = 1
    if pagetype == 'pagedown':
        curpage += 1
    elif pagetype == 'pageup':
        curpage -= 1
    elif pagetype == 'pageto':
        pass
    startpos = (curpage - 1) * GPageCount
    endpos = startpos + GPageCount
    games = GameInfo.objects.all()[startpos:endpos]
    if curpage == 1 and allpage == 1:
        allNewsCount = GameInfo.objects.count()
        allpage = allNewsCount // GPageCount
        remainPost = allNewsCount % GPageCount
        if remainPost > 0:
            allpage += 1
    pagelist = []  # below are the logic of pagination
    if(allpage - curpage > GPAGERLEN - 2):
        for i in range(curpage - 1 - GPAGERLEN // 2 if curpage - 1 - GPAGERLEN // 2 > 0 else 0, curpage - 1 + GPAGERLEN // 2):
            pagelist.append(i + 1)
            if len(pagelist) > GPAGERLEN - 1:
                break
    else:
        if (curpage - 1 - GPAGERLEN // 2 > 0):
            for i in range(curpage - 1 - GPAGERLEN // 2, curpage - 1 + GPAGERLEN // 2 if curpage - 1 + GPAGERLEN // 2 < allpage else allpage):
                pagelist.append(i + 1)
                if len(pagelist) > GPAGERLEN - 1:
                    break
        else:
            for i in range(0, curpage - 1 + GPAGERLEN // 2 if curpage - 1 + GPAGERLEN // 2 < allpage else allpage):
                pagelist.append(i + 1)
                if len(pagelist) > GPAGERLEN - 1:
                    break
    
    return render(request,'GameCenter.html',{'gamelist': games, 'allpage': allpage, 'borderpage': allpage - 3, 'pagelist': pagelist, 'curpage': curpage, 'gm': game, 'gc': gc})


def BalagwIndex(request):
    return render_to_response('balagwindex.html')


def fenxiang(request):
    return render_to_response('fenxiang.html')


def fenxiang2(request):
    return render_to_response('fenxiang2.html')


def bbindex(request):
    return render_to_response('bbindex.html')


def balala2fx(request):
    return render_to_response('balala2fxindex.html')


def h5fenindex(request):
    return render_to_response('h5fenindex.html')
