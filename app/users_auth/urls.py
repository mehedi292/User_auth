from django.urls import path
from .views import home, register, login_user, logout_user
from app.users_auth import views

urlpatterns = [
    path('home/', home, name="home"),
    path('register/', register, name="register"),
    path('login_user/', login_user, name="login_user"),
    path('logout_user/', logout_user, name="logout_user"),
    path('password_change/', views.change_password, name='change_password'),
]