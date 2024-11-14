from django.contrib import admin
from django.urls import path
from myFirstApp import views

urlpatterns = [
    path('', views.index, name="home"),
    path('sports/', views.sports, name="sports"),
    path('entertainment/', views.entertainment, name="entertainment"),
    path('politics/', views.politics, name="politics")

]
