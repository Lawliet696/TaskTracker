from django.urls import path
from .views import list_tasks, create_task, edit_task, detail_task, completed_list_tasks, delete_task

app_name = 'tasks'

urlpatterns = [
    path('', list_tasks, name='task_list'),
    path('create/', create_task, name='create_task'),
    path('completed/', completed_list_tasks, name='completed_list_tasks'),
    path('edit/<uuid:uuid>/', edit_task, name='edit_task'),
    path('<uuid:uuid>/', detail_task, name="detail_task"),
    path('edit/<uuid:uuid>/delete/', delete_task, name='delete_task'),
]