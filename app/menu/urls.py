from django.urls import path

from menu import views

urlpatterns = [
    path("", views.PageView.as_view()),
]
