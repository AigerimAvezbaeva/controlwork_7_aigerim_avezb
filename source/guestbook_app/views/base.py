from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
from guestbook_app.models import GuestBook
from guestbook_app.forms import GuestBookForm


def index_view(request: WSGIRequest):
    if request.method == 'GET':
        guestsbook = GuestBook.objects.filter(status='active')
        form = GuestBookForm()
        return render(request, 'guestbook_index.html', context={
            'form': form,
            'guests': guestsbook
        })
    guestsbook = GuestBook.objects.filter(status='active')
    form = GuestBookForm(data=request.POST)
    if not form.is_valid():
        return render(request, 'guestbook_index.html', context={
            'form': form,
            'guests': guestsbook
        })
    else:
        guestbook = GuestBook.objects.create(**form.cleaned_data)
        return redirect('index')
    # return render(request, 'guestbook_index.html', context=context)
