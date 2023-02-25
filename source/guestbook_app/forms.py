from django import forms
from guestbook_app.models import GuestBook


class GuestBookForm(forms.ModelForm):
    class Meta:
        model = GuestBook
        fields = ('fullname', 'email', 'text')
