from django.urls import path
from home import views
urlpatterns = [
    path('', views.home, name="home"),
    path('certificate/', views.certificate, name="certificate"),
    path('progress/', views.progress, name="progress"),
    path('course/', views.course, name="course"),
    path('frontend/', views.frontend, name="frontend"),
]