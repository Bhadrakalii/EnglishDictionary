from django.contrib import admin
from django.urls import path
from dictionary import views

urlpatterns = [
    path('', views.index, name = 'dictionary'),
    path('contact',views.contact, name = 'contact'),
    path('results', views.results, name = 'results' )
]