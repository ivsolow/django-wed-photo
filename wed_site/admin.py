from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(MainPhotos)
admin.site.register(LoveStories)
admin.site.register(Feedback)


class ImgSeriesAdmin(admin.StackedInline):
    model = ImgSeries


@admin.register(WedPost)
class WedPostAdmin(admin.ModelAdmin):
    inlines = [ImgSeriesAdmin]


@admin.register(ImgSeries)
class ImgSeriesAdmin(admin.ModelAdmin):
    pass

