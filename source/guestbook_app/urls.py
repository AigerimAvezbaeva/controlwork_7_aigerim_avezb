from django.urls import path
from guestbook_app.views.base import index_view
from guestbook_app.views.guestbook_views import add_guest, update_guestbook, delete_guest, confirm_delete

urlpatterns = [
    path('', index_view, name='index'),
    path('guestbook/', index_view, name='index'),
    path('guestbook/add_guest', add_guest, name='add_guest'),
    path('guestbook/<int:pk>/update', update_guestbook, name='update_guest'),
    path('guestbook/<int:pk>/delete', delete_guest, name='delete_guest'),
    path('guestbook/<int:pk>/confirm_delete', confirm_delete, name='confirm_delete')
]
