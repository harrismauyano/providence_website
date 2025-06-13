from django.shortcuts import render

# Create your views here.
# Each function renders a page
def home(request):
    return render(request, 'main/home.html')

def results(request):
    return render(request, 'main/results.html')

def admissions(request):
    return render(request, 'main/admissions.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')


def about_developer(request):
    return render(request, 'main/developer_info.html')


def events(request):
    return render(request, 'main/events.html')


def announcements(request):
    return render(request, 'main/announcements.html')


def blog(request):
    return render(request, 'main/blog.html')

