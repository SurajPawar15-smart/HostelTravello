from django.urls import path
from . import views

urlpatterns = [
    path("register", views.register,name="register"),
    path("login", views.login,name="login"),
    path("logout", views.logout,name="logout"),
    path("contact", views.contact,name="contact"),
    path("home", views.home,name="home"),
    path("services", views.services,name="services"),
    path("about", views.about,name="about"),
    path("news", views.news,name="news"),

]