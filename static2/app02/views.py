from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home2.html',{"info":"i have a headache lol"})