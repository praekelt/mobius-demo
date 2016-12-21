from django.conf.urls import url, include
from django.views.generic.base import TemplateView


urlpatterns = [
    url(
        r"^$",
        TemplateView.as_view(template_name="demo/home.html"),
        name="home"
    )
]
