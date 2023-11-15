from django.conf import settings
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from .excel import *
from .forms import AdminPanelForm
from .models import Group, WeekSchedule


class Home(ListView):
    template_name = 'schedule/index.html'
    context_object_name = 'groups'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Главная"
        context['courses'] = ['Первый', 'Второй', 'Третий', 'Четвертый']
        return context

    def get_queryset(self):
        return Group.objects.order_by('title')


class Schedule(DetailView):
    model = Group
    context_object_name = 'group'
    template_name = 'schedule/schedule_group.html'





def admin_panel(request):
    if request.method == "POST":
        form = AdminPanelForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['file']
            fs = FileSystemStorage(location=settings.EXCEL_ROOT)
            fs.save(excel_file.name, excel_file)
            messages.success(request, message="Успешно")

            group = Group.objects.get(title="23ИСИТ 1гр")
            group.content = get_week_schedule(get_ws(), RANGES_GROUPS["23ИСИТ 1гр"][0])
            group.save()
            print(group.content)

            return redirect('home')
        else:
            messages.error(request, message="Не успешно")
    else:
        form = AdminPanelForm(request.POST, request.FILES)
    context = {
        'title': 'Админ-панель',
        'form': form
    }
    return render(request, template_name='schedule/admin_panel.html', context=context)


