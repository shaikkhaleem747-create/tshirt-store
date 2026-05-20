from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('signup/', views.signup, name='signup'),

    path('login/', views.userlogin, name='login'),

    path('logout/', views.userlogout, name='logout'),

    path('product/<int:id>/', views.detail, name='detail'),

    path('buy/<int:id>/', views.buy, name='buy'),

    path('history/', views.history, name='history'),

    path('clearhistory/', views.clearhistory, name='clearhistory'),

    path('contact/', views.contact, name='contact'),

    path('api/tshirts/', views.tshirt_api),

    path('api/orders/', views.order_api),

]