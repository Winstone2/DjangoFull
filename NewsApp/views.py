from django.shortcuts import render, HttpResponse

# Create your views here.

def Home(request):
    return render(request, 'home.html')

def News(request):
    return render(request, 'News.html')
def Contact(request):
    return render(request, 'Contact.html')