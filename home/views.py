from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html')
def certificate(request):
    return render(request, 'certificate.html')
def progress(request):
    return render(request, 'progress.html')
def course(request):
    return render(request, 'course.html')
def frontend(request):
    return render(request, 'roadmap/frontend.html')
def signin(request):
    if request.method == "POST":
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully.")
            return render(request, "home.html")
        else:
            messages.error(request, "Bad credentials")
            return redirect("home")
    return render(request, "home.html")
def signup(request):
    if request.method == "POST":
        user = User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            password=request.POST['password'],
            )
        user.first_name =  request.POST['fname']
        user.last_name = request.POST['lname']
        user.is_active = False
        user.save()
        messages.success(request, "You have successfully signed up. please login!")
        return redirect('home')
    return render(request, 'home.html')
def signout(request):
    logout(request)
    return redirect('home')