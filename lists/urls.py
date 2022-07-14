from django.urls import path

from lists import views

urlpatterns = [
    path('home/', views.home_page, name='home'),
]