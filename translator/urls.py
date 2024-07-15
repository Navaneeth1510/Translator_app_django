from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_main, name='mainpage'),
    path('login_auth/', views.login_auth, name='login_auth'),
    path('signup_auth/', views.register, name='signup_auth'),
    path('mainpage.html/', views.show_main, name='mainpage'),
    path('sign_up.html/', views.show_signup, name='signup'),
    path('loginpage.html/', views.show_login, name='loginpage'),
    path('translator.html/', views.translator, name='translator'),
    path('translator/', views.translator, name='translator'),
    path('translator/translated/', views.translated, name='translated'),
]
