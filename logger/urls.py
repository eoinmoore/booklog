from django.urls import path

from . import views

app_name = "logger"

urlpatterns = [
    # ie: /logger/
    path('', views.index, name='index'),
    # ie: /logger/list
    path('list', views.ListView.as_view(), name='list'),
    # ie: /logger/5
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ie: /logger/log
    path('log', views.log, name="log"),
]
