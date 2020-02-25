from django.urls import path

from . import views

app_name = 'xmlapp'
urlpatterns = [
    path('',views.index, name='index'),
    path('ActivityDateType', views.ActivityDateType, name='ActivityDateType')    
]