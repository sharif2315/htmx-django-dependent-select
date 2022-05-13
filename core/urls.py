from django.urls import path
from . import views


urlpatterns = [
    path('', views.courses, name=''),
    path('modules/', views.modules, name='modules'),
    path('submodules/', views.submodules, name='submodules'),
]
