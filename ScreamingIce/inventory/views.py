from django.shortcuts import render
from .models import IceCream


def scream_maker(request):

    """
    Creates a new Ice Cream record in the database
    from the user's submitted form data

    A view is a function that takes HTTP request
    and returns an HTTP response

    """
    pass
    return render(request, 'index.html')



def scream_taker(request, pk):

    """
    Retrieve a new Ice Cream record in the database
    from the URL.

    """

    icecream = IceCream.objects.get(pk=pk)

    context = {'scream': icecream}

    pass
    return render(request, 'index.html', context)