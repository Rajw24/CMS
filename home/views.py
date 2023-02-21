from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from home.tokens import generate_token
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

        #Welcome Email
        subject = "Welcome to CMS"
        message = f"Hello {user.first_name} {user.last_name} !!\nWelcome to CMS. Thank you for Signing up \nWe have also sent you a conformation email, please confirm your email address in order to activate your account." 
        from_email = info.EMAIL_HOST_USER
        to_email = [user.email]
        send_mail(subject, message, from_email, to_email, fail_silently=False)

        #Confirmation email
        current_site = get_current_site(request)
        email_subject = "Email Verification at CMS"
        email_message = render_to_string("email.html", {
            'name' : user.first_name,
            'domain' : current_site.domain,
            'uid' : urlsafe_base64_encode(force_bytes(user.pk)),
            'token': generate_token.make_token(user)
        })
        Confirmation_email = EmailMessage(
            email_subject,
            email_message,
            from_email,
            to_email,
        ) 

        Confirmation_email.fail_silently = True
        Confirmation_email.send()

        messages.success(request, "You have successfully signed up. please check your E-mail to login!")
        return redirect('home')
    return render(request, 'home.html')

def signout(request):
    logout(request)
    messages.success(request, "Loged out Successfully.")
    return redirect('home')

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and generate_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('home') 
    else:
        return render(request, 'Activation_failed.html')