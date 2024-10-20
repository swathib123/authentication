
from django.urls import path
from .import views

urlpatterns = [
    
    path('manager/',views.custommanager),
    path('manager/<int:id>',views.manager_id),
    path('supervisor/',views.customsupervisor),
    path('supervisor/<int:id>',views.supervisor_id),
    
]