from django.urls import path
from web import views

urlpatterns = [
    path('', views.index, name='index'),
    path('execute/', views.index, name='index'),
    path('show-history/', views.index, name='index')
]
