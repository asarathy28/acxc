from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('short/', views.short, name='short'),
    path('medium/', views.medium, name='medium'),
    path('long/', views.long, name='long'),
    path('truely-long/', views.truelyLong, name='truelyLong'),
    path('destination/', views.destination, name='destination'),
]
