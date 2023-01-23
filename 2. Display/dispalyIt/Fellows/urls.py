from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='mainHomePage'),
    path('Fellows/', views.index, name='index'),
    path('Fellows/details/<int:id>', views.details, name='details'),
    path('testing/', views.test, name='test')
]