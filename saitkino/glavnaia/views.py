from django.shortcuts import render

# Create your views here.

def glavnaia(reguest):
    return render(reguest, 'glavnaia.html')
