from django.shortcuts import render
from django.shortcuts import render_to_response
from NineCo.models import JobsInfo, Classification, GameInfo, GameClass, News


def Index(request):
    return render_to_response("index.html")


def summary(request):
    return render_to_response("summary.html")


def contact(request):
    return render(request, "contact.html")


def jobs(request):
    jobsinfos = JobsInfo.objects.all().order_by('-dimDate')
    classifications = Classification.objects.all()
    return render_to_response("jobs.html", {'jb': jobsinfos, 'cl': classifications})


def gamelist(request):
    games = GameInfo.objects.all().order_by('-dimDate')
    return render_to_response("gamelist.html", {'gm': games})


def gamecl(request):
    games = GameInfo.objects.all().order_by('-dimDate')
    gc = GameClass.objects.all()
    return render_to_response("allgame.html", {'gm': games, 'gc': gc})


PageCount = 1
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
        # if (curpage - 1 - PAGERLEN // 2 > 0):
            for i in range(curpage - 1 - PAGERLEN // 2, curpage - 1 + PAGERLEN // 2 if curpage - 1 + PAGERLEN // 2 < allpage else allpage):
                pagelist.append(i + 1)
                if len(pagelist) > PAGERLEN - 1:
                    break

    return render_to_response('News.html', {'news': posts, 'allpage': allpage, 'borderpage': allpage - 3, 'pagelist': pagelist, 'curpage': curpage})


def gamed(request, i):
    game = GameInfo.objects.get(id=i)
    game.imgUrl = 'img/' + game.imgUrl.split('/')[-1]
    game.QRimg = 'img/' + game.QRimg.split('/')[-1]
    game.Url = 'apps/' + game.Url.split('/')[-1]
    game.imgContent1 = 'img/' + game.imgContent1.split('/')[-1]
    game.imgContent2 = 'img/' + game.imgContent2.split('/')[-1]
    game.imgContent3 = 'img/' + game.imgContent3.split('/')[-1]
    return render_to_response('showgame.html', {'game': game})
