from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('',views.home,name='crypto-home'),
    path('graphs/',views.graphs,name='crypto-graphs'),
    path('realTimeGraph/',views.realTime,name='crypto-realtime')
]