from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_info, name='base_info'),
    path('download/', views.download_resume, name='download_resume')
]