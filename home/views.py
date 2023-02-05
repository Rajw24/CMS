from django.shortcuts import render

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
