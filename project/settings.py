from project.settings_mobius import *


# Out app must be first
INSTALLED_APPS = list(INSTALLED_APPS)
INSTALLED_APPS = ["demo"] + INSTALLED_APPS

# Configuration for our app
DEMO = {
}

# Until Salt drives settings_local we need this in here
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "mobius",
        "USER": "mobius",
        "PASSWORD": "afdc6b255",
        "HOST": "10.10.0.1",
        "PORT": "5432",
    }
}

# Typically used in actual deploys
try:
    import settings_local
    from settings_local import *
except ImportError:
    pass
else:
    if hasattr(settings_local, "configure"):
        lcl = locals()
        di = settings_local.configure(**locals())
        lcl.update(**di)
