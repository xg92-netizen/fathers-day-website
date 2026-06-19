from django.contrib import admin

from .models import Enter


@admin.register(Enter)
class EnterAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'phone')
    search_fields = ('username', 'phone')
    ordering = ('-id',)
