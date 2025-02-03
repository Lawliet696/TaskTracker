from django.urls import path
from .views import show_profile

app_name = 'users'

urlpatterns = [
    path('', show_profile, name='show_profile'),
]