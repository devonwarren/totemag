from .base import *

DEBUG = True

TEMPLATES[0]['OPTIONS']['debug'] = True

INSTALLED_APPS += ("debug_toolbar", )
INTERNAL_IPS = ("127.0.0.1",)
MIDDLEWARE_CLASSES += \
    ("debug_toolbar.middleware.DebugToolbarMiddleware", )

