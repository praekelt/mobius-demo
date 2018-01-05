from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from ultracache.decorators import cached_get
from demo.forms import TestForm
from demo.models import TrivialContent


class TestView(FormView):
    template_name = "demo/test_view.html"
    form_class = TestForm


# Four views to illustrate django-ultracache and django-cache-headers working
# together.

@method_decorator(
    cached_get(600), name="get"
)
class AllUsersView(TemplateView):
    template_name = "demo/all_users_view.html"

    def get_context_data(self, **kwargs):
        di = super(AllUsersView, self).get_context_data(**kwargs)
        di["object"] = TrivialContent.objects.get(id=1)
        return di


# We can't use the cached_get decorator because the view  may not be cached for
# authenticated users. We need to use template fragment caching.
class AnonymousOnlyView(TemplateView):
    template_name = "demo/anonymous_only_view.html"

    def get_context_data(self, **kwargs):
        di = super(AnonymousOnlyView, self).get_context_data(**kwargs)
        di["object"] = TrivialContent.objects.get(id=2)
        return di


@method_decorator(
    cached_get(600, "request.user.is_authenticated()"), name="get"
)
class AnonymousAndAuthenticatedView(TemplateView):
    template_name = "demo/anonymous_and_authenticated_view.html"

    def get_context_data(self, **kwargs):
        di = super(AnonymousAndAuthenticatedView, self).get_context_data(**kwargs)
        di["object"] = TrivialContent.objects.get(id=3)
        return di


@method_decorator(
    cached_get(600, "request.user.id"), name="get"
)
class PerUserView(TemplateView):
    template_name = "demo/per_user_view.html"

    def get_context_data(self, **kwargs):
        di = super(PerUserView, self).get_context_data(**kwargs)
        di["object"] = TrivialContent.objects.get(id=4)
        return di
