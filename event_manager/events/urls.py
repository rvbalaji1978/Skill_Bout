"""
URL configuration for event_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
<<<<<<< HEAD
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
=======
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
>>>>>>> 03f94ea (Initial upload of event manager project)
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("edit-event/<int:pk>/", views.EditEvent, name="edit_event"),
    path("delete-event/<int:pk>/", views.DeleteEvent, name="delete_event"),
    path("delete_review/<int:pk>", views.DeleteReview, name="delete_review"),
    path("edit_review/<int:pk>", views.EditReview, name="edit_review"),
    path("dash/", views.DashView.as_view(), name="dash"),
    path("login/", views.LoginView, name="login"),
    path("register/", views.RegisterView, name="register"),
    path("logout/", views.LogoutView, name="logout"),
    path("profile/", views.ProfileView, name="profile"),
    path("add-event/", views.AddEvent, name="add-event"),
    path("buy-ticket/<int:pk>", views.BuyTicket, name="buy-ticket"),
    path("details/<int:pk>", views.PublicDetails, name="details"),
    path("review/<int:pk>", views.AddReview, name="add-review"),
]
