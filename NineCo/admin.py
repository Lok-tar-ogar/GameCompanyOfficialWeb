from django.contrib import admin
from NineCo.models import Carousel, Classification, GameClass, GameInfo, JobsInfo, News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('newsTitle', 'newsDetail', 'viewedTimes', 'dimDate')
    search_fields = ('newsTitle')
admin.site.register(News)
