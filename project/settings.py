from project.settings_mobius import *


# Out app must be first
INSTALLED_APPS = list(INSTALLED_APPS)
INSTALLED_APPS = ["demo"] + INSTALLED_APPS

# Configuration for our app
DEMO = {
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
