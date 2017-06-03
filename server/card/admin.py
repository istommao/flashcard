"""card admin."""
from django.contrib import admin

from card.models import Card


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    """Card admin."""

    list_display = ('name', 'creation_time', 'updation_time')

    readonly_fields = ('uid', 'creation_time', 'updation_time')
