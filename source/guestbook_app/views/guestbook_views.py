from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404
from guestbook_app.forms import GuestBookForm
from guestbook_app.models import GuestBook


def add_guest(request: WSGIRequest):
    if request.method == 'GET':
        form = GuestBookForm()
        return render(request, 'add_guest.html', context={
            'form': form
        })

    form = GuestBookForm(data=request.POST)
    if not form.is_valid():
        return render(request, 'add_guest.html', context={
            'form': form
        })
    else:
        guestbook = GuestBook.objects.create(**form.cleaned_data)
        return redirect('index')


def update_guestbook(request, pk):
    errors ={}
    guestbook = get_object_or_404(GuestBook, pk=pk)
    form = GuestBookForm(instance=guestbook)
    if request.method == 'POST':
        form = GuestBookForm(request.POST, instance=guestbook)
        if not request.POST.get('fullname'):
            errors['title'] = 'Данное поле обязательно к заполнению'
        guestbook.fullname = request.POST.get('fullname')
        guestbook.email = request.POST.get('email')
        guestbook.text = request.POST.get('text')
        if errors:
            return render(request, 'guestbook_update.html', context={
                'guest': guestbook,
                'form': form,
                'errors': errors
            })
        form.save()
        return redirect('index')
    return render(request, 'guestbook_update.html', context={
        'guest': guestbook,
        'form': form
    })


def delete_guest(request, pk):
    guestbook = get_object_or_404(GuestBook, pk=pk)
    return render(request, 'confirm_delete.html', context={
        'guest': guestbook
    })


def confirm_delete(request, pk):
    guestbook = get_object_or_404(GuestBook, pk=pk)
    guestbook.delete()
    return redirect('index')
