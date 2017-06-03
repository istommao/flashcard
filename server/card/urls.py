"""info urls module."""
from extension.utils import generate_urlpatterns

from card import views


URLS = [
    ('^$', views.IndexView),
]

# pylint: disable=C0103
urlpatterns = generate_urlpatterns(URLS)
