from django.shortcuts import render



# Create your views here.
def page1(request):
    return render(request, "page1.html",{'navbar':'page1'})


def page2(request):
    return render(request, "page2.html",{'navbar':'page2'})


def page3(request):
    return render(request, "page3.html",{'navbar':'page3'})

def page2(request):
    return render(request, "login.html")
