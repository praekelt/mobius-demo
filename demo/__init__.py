from django.conf import settings

SETTINGS = {}
try:
    SETTINGS.update(settings.DEMO)
except AttributeError:
    # No overrides
    pass
