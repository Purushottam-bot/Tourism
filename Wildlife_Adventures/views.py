from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'Wildlife_Adventures/home03.html')
