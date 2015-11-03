from django.contrib import admin
from NineCo.models import Carousel, Classification, GameClass, GameInfo, JobsInfo, News


class NewsAdmin(admin.ModelAdmin):

    class Media:
        js = (

            '/static/tinymce/tinymce.min.js',
            '/static/tinymce/config.js',

        )
admin.site.register(News, NewsAdmin)
admin.site.register(GameClass)
admin.site.register(GameInfo)
admin.site.register(JobsInfo)
admin.site.register(Carousel)
admin.site.register(Classification)
