from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "myFirstApp/index.html")

def politics(request):
    return render(request, "myFirstApp/politics.html")

def sports(request):
    return render(request, "myFirstApp/sports.html")

def entertainment(request):
    return render(request, "myFirstApp/entertainment.html")