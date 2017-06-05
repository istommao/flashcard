"""card views."""
from django.views import generic

from card.models import Card


class IndexView(generic.TemplateView):
    """Index view."""

    view_name = 'index'

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        card = Card.objects.first()

        dataset = {'card': card}
        context.update(dataset)
        return context
