from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('payment/',views.payment,name="payment"),
    path('createEvent/<str:pk>/',views.createEvent,name="createEvent"),

]