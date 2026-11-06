from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_task, name='add_task'),
    path('done/<int:task_id>/', views.mark_done, name='mark_done'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
]