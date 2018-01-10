from django.conf.urls import url, include
from django.views.generic.base import TemplateView

from demo import views


urlpatterns = [
    url(
        r"^$",
        TemplateView.as_view(template_name="demo/home.html"),
        name="home"
    ),
    url(
        r"^all-users/$",
        views.AllUsersView.as_view(),
        name="all-users"
    ),
    url(
        r"^anonymous-only/$",
        views.AnonymousOnlyView.as_view(),
        name="anonymous-only"
    ),
    url(
        r"^anonymous-and-authenticated/$",
        views.AnonymousAndAuthenticatedView.as_view(),
        name="anonymous-and-authenticated"
    ),
    url(
        r"^per-user/$",
        views.PerUserView.as_view(),
        name="per-user"
    ),
    url(
        r"^modify/(?P<pk>\d+)/$",
        views.modify_trivial_content,
        name="modify-trivial-content"
    ),
]
