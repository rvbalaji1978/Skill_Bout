"""
ASGI config for event_manager project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
=======
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
>>>>>>> 03f94ea (Initial upload of event manager project)
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'event_manager.settings')

application = get_asgi_application()
