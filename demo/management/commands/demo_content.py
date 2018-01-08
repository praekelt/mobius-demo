from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError

from demo.models import TrivialContent


class Command(BaseCommand):

    def handle(self, *args, **options):

        # Super user
        user = User.objects.create(username="admin", is_superuser=1, is_staff=1)
        user.set_password("local")
        user.save()

        # Content
        for title, slug in (
            ("All users", "all-users"),
            ("Anonymous only", "anonymous-only"),
            ("Anonymous and authenticated", "anonymous-and-authenticated"),
            ("Per user", "per-user")
        ):
            TrivialContent.objects.create(title=title, slug=slug)
