from django.urls import path
from .views import register_manager, login_manager

urlpatterns = [
    path('register/', register_manager, name='register_manager'),
    path('login/', login_manager, name='login_manager'),
]
