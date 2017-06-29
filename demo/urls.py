from django.conf.urls import url, include
from django.views.generic.base import TemplateView


urlpatterns = [
    url(
        r"^radmin/",
        TemplateView.as_view(template_name="demo/radmin.html"),
        name="radmin"
    ),
    url(
        r"^$",
        TemplateView.as_view(template_name="demo/home.html"),
        name="home"
    )
]
