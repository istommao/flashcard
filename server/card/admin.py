"""card admin."""
from django import forms
from django.contrib import admin

from card.models import Card


class CardAdminForm(forms.ModelForm):
    """CardAdmin form."""
    short_intro = forms.CharField(label='简介',
                                  widget=forms.Textarea)


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    """Card admin."""

    form = CardAdminForm

    list_display = ('name', 'creation_time', 'updation_time')

    readonly_fields = ('uid', 'creation_time', 'updation_time')
