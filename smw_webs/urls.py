from django.urls import path

from. import views

app_name = 'views'

urlpatterns = [
    path('', views.index, name='index'),
    path('events/', views.events, name='events'),
    path('contact/', views.contact, name='contact'),
    path('oday/', views.oday, name='oday'),
]