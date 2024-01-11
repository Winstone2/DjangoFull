from django.shortcuts import render, HttpResponse

# Create your views here.

def Home(request):
    context={
        "name": "Marjesty Owino",
        "number": 1123
    }
    return render(request, 'home.html', context)

def News(request):
    context={
        "list": ["python", "django", "kotlin", "C++", "Javascript", "Java"],
        "mynum": 50
    }
    return render(request, 'News.html', context)
def Contact(request):
    return render(request, 'Contact.html',)