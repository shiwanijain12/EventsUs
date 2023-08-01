from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('payment/',views.payment,name="payment"),
    path('event_list/', views.event_list, name='event_list'),
    path('event_detail/<int:event_id>/', views.event_detail, name='event_detail'),
    path('event_registration/<int:event_id>', views.event_registration, name='event_registration'),
    path('organizer_registration/', views.organizer_registration, name='organizer_registration'),
    path('client_registration/', views.client_registration, name='client_registration'),
    path('create_event/', views.create_event, name='create_event'),
    path('<int:event_id>/feedback/', views.event_feedback, name='event_feedback'),

]