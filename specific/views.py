from django.shortcuts import render

# Create your views here.
def sasuke(request):
    return render(request,'sasuke.html')

def itachi(request):
    return render(request,'itachi.html')


