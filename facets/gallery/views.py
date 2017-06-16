from django.shortcuts import render, redirect
from .models import Media
from gallery.forms import MediaModelForm
from django.contrib import messages



def create(request):
    """
    creates one media upload file entry

    """

    # Allows a filled-out form to be submitted and stored in database and redirect to Gallery web page
    if request.method == 'GET':
        form = MediaModelForm()
    elif request.method == 'POST':
        form = MediaModelForm(data=request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('/gallery/display')

    context = {'form': form}
    return render(request,'create.html', context)


def retreive(request, pk):
    """
    retrieves one media file in database

    """

    media = Media.objects.get(id=pk)
    context = {'media': media}
    return render(request, 'details.html', context)


def update(request, pk):
    """
    updates one media file in database

    """
    media = Media.objects.get(id=pk)


    # Allows a filled-out form to be updated and stored in database then user redirected to Gallery web page
    if request.method == 'GET':
        form = MediaModelForm(instance=media)
    elif request.method == 'POST':
        form = MediaModelForm(instance=media, data=request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.add_message(request, messages.INFO, f'{media.name.upper()} has been Updated!')
            return redirect('/gallery/display')


    context = {'form': form}
    return render(request, 'create.html', context)


def delete(request, pk):
    """
    deletes one media file or group in database

    """

    media = Media.objects.get(id=pk)
    context = {'status': f"Deleted {media.id}"}
    return render(request, 'base.html', context)


def display(request):
    """
    display one media file entry

    """

    context = {}
    return render(request, 'details.html', context)