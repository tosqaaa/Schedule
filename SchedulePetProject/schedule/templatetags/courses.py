from django import template

from ..models import Group

register = template.Library()


@register.inclusion_tag('schedule/course_tmpl.html')
def show_course_groups(course):
    course_groups = Group.objects.filter(course=course)
    course_groups_with_subgroups = Group.objects.filter(course=course)
    return {'course_groups': course_groups,}
            # 'course_groups_with_subgroups': course_groups_with_subgroups}
