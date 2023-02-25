from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from guestbook_app.models import GuestBook


def index_view(request: WSGIRequest):
    guestsbook = GuestBook.objects.filter(status='active')
    context = {
        'guests': guestsbook
    }
    return render(request, 'guestbook_index.html', context=context)
