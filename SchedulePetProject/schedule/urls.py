from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import Home, Schedule, admin_panel

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('schedule/<str:slug>', Schedule.as_view(), name='schedule'),
    path('admin-panel/', admin_panel, name='admin_panel'),
]

urlpatterns = [

              ] + urlpatterns
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
