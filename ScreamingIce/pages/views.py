from django.shortcuts import render

# Create your views here.

def home(request):
    """
    Renders the landing page.

    """
    return render(request, 'home.html')