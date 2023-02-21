from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail
from CMS import info

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
        
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        if User.objects.filter(username=username):
            messages.error(request, "Username Already Exists.")
            return redirect('home')
        
        if User.objects.filter(email=email):
            messages.error(request, "Email is Already resistered.")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, "Username Can only containe Alphabets and numbers.")
            return redirect('home')

        if len(str(password)) < 8:
            messages.error(request, "Password must be 8 Character long")
            return redirect('home')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            )
        user.first_name =  request.POST['fname']
        user.last_name = request.POST['lname']
        user.is_active = False
        user.save()

        subject = "Welcome to CMS"
        message = f"Hello {user.first_name} !!\nWelcome to CMS. Thank you for Signing up \nWe have also sent you a conformation email, please confirm your email address in order to activate your account." 
        from_email = info.EMAIL_HOST_USER
        to_email = [user.email]
        send_mail(subject, message, from_email, to_email, fail_silently=False)

        messages.success(request, "You have successfully signed up. please login!")
        return redirect('home')
    return render(request, 'home.html')
def signout(request):
    logout(request)
    messages.success(request, "Loged out Successfully.")
    return redirect('home')