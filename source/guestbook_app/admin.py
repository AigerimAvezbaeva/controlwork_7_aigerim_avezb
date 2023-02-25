from django.contrib import admin

from guestbook_app.models import GuestBook


# Register your models here.
class GuestBookAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullname', 'status', 'created_at')
    list_filter = ('id', 'fullname', 'status', 'created_at')
    search_fields = ('fullname', 'status')
    list_editable = ('fullname', 'status')


admin.site.register(GuestBook, GuestBookAdmin)
