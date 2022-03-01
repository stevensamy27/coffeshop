from . import views
from django.urls import path

urlpatterns = [
    path('', views.defult, name = 'defult'),
    path('my1', views.my1, name = 'my1'),

]