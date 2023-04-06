from django.urls import path
from home import views
urlpatterns = [
    path('', views.home, name="home"),
    path('certificate/', views.certificate, name="certificate"),
    path('progress/', views.progress, name="progress"),
    path('course/', views.course, name="course"),
    path('frontend/', views.frontend, name="frontend"),
    path('backend/', views.backend, name="backend"),
    path('android/', views.android, name="android"),
    path('devops/', views.devops, name="devops"),
    path('database/', views.database, name="database"),
    path('quality/', views.quality, name="quality"),
    path('software/', views.software, name="software"),
    path('blockchain/', views.blockchain, name="blockchain"),
    path('fullstack/', views.fullstack, name="fullstack"),
    path('signin/', views.signin, name="signin"),
    path('signup/', views.signup, name="signup"),
    path('signout/', views.signout, name="signout"),
    path('contact/', views.contact, name="contact"),
    path('activate/<uidb64>/<token>', views.activate, name="activate"),
]