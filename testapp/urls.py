from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('product/<int:id>/', views.detail, name='detail'),

    path('buy/<int:id>/', views.buy, name='buy'),

    path('history/', views.history, name='history'),

    path('contact/', views.contact, name='contact'),

]