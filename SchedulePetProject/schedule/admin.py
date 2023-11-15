from django.contrib import admin

from .models import Group, WeekSchedule


class GroupAdmin(admin.ModelAdmin):
    list_display_links = ('pk',)
    list_display = ('pk', 'title', 'course',)
    search_fields = ('title',)
    list_filter = ('course',)
    list_editable = ('title', 'course')
    prepopulated_fields = {'slug': ('title',)}


class WeekScheduleAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Group, GroupAdmin)
admin.site.register(WeekSchedule, WeekScheduleAdmin)
