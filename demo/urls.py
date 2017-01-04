from django.conf.urls import url, include
from django.views.generic.base import TemplateView

from demo.views import TestView


urlpatterns = [
    url(
        r"^$",
        TemplateView.as_view(template_name="demo/home.html"),
        name="home"
    ),
    url(
        r"^test-view/$",
        TestView.as_view(),
        name="test-view"
    )
]
