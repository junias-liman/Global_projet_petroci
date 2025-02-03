from django.shortcuts import render

# Create your views here.
def home_general(request):
    return render(request,'home.html')

def entete(request):
    return render(request,'tete.html')

