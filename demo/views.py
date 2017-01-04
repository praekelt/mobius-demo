from django.views.generic.edit import FormView

from demo.forms import TestForm


class TestView(FormView):
    template_name = "demo/test_view.html"
    form_class = TestForm
