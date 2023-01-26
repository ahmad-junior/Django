from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name="HomePage"),
    path('Fellows/', views.mainDataBase, name="DataBaseFellows")
]
