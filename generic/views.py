from django.shortcuts import render

# Create your views here.
def naruto(request):
    return render(request,'naruto.html')

def jiraya(request):
    return render(request,'jiraya.html')

