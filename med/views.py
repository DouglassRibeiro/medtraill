from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'med/homepage.html')

def homepage_register(request):
    return render(request, 'med/homepage_register.html')