from django.contrib import admin
from .models import *


class what_You_learn_TabularInline(admin.TabularInline):
    model = What_You_learn


class Requirements_TabularInline(admin.TabularInline):
    model = Requirements


class Video_TabularInline(admin.TabularInline):
    model = Video


class course_admin(admin.ModelAdmin):
    inlines = (what_You_learn_TabularInline,Requirements_TabularInline, Video_TabularInline)


admin.site.register(Categories)
admin.site.register(Author)
admin.site.register(Course, course_admin)
admin.site.register(Level)
admin.site.register(What_You_learn)
admin.site.register(Requirements)
admin.site.register(Lesson)
admin.site.register(UserCourse)
admin.site.register(Video)
