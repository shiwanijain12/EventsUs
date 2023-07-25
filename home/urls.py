from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('payment/',views.payment,name="payment"),
    path('event_list', views.event_list, name='event_list'),
    path('event_detail/<int:event_id>/', views.event_detail, name='event_detail'),
    path('registration/<int:event_id>', views.event_registration, name='event_registration'),

]