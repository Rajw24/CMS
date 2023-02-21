from django.urls import path
from home import views
urlpatterns = [
    path('', views.home, name="home"),
    path('certificate/', views.certificate, name="certificate"),
    path('progress/', views.progress, name="progress"),
    path('course/', views.course, name="course"),
    path('frontend/', views.frontend, name="frontend"),
    path('signin/', views.signin, name="signin"),
    path('signup/', views.signup, name="signup"),
    path('signout/', views.signout, name="signout"),
    path('activate/<uidb64>/<token>', views.activate, name="activate"),
]