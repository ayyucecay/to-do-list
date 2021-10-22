from django.shortcuts import render
from django.shortcuts import redirect

def random_view(request):
    return render(request, '../templates/main.html')
