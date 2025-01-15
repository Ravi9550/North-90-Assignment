from django.urls import path
from . import views

urlpatterns = [
    path('singlechat', views.singlechat, name='singlechat'),
    path('profile/', views.profile, name='profile'),
    path('signup/', views.registerview, name='signup'),
    path('', views.loginview, name='login'),
    path('logout/', views.logoutview, name='logout'),
    path('chat/get_old_messages/<str:username>/', views.get_old_messages, name='get_old_messages'),

]