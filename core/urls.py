from django.urls import path
from . import views


urlpatterns = [
    path('', views.courses_view, name=''),
    path('modules/', views.modules_view, name='modules'),
    path('submodules/', views.submodules_view, name='submodules'),
]
