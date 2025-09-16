from django.urls import path, re_path
from django.contrib import admin
from data_admins import views as admins

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', admins.index, name="index"),
    path('user/register/', admins.register, name="register"),
    path('user/add_data/', admins.add_data, name="add_data"),
    path('user/userpage/', admins.userpage, name="userpage"),
    path('user/labeled_data/', admins.labeled_data, name="labeled_data"),
    path('user/unlabeled_data/', admins.unlabeled_data, name="unlabeled_data"),
    path('user/ddos_analysis/', admins.ddos_analysis, name="ddos_analysis"),
    re_path(r'^user/chart_page/(?P<chart_type>\w+)/$', admins.chart_page, name="chart_page"),
]