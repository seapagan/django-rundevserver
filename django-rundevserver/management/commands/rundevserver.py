"""Custom command to run the dev server.

This allows us to set specific settings for the dev server in the projects
'settings.py' file using the following names :

# set the port to run the dev server on, default is 8000
RDS_PORT = "8000"

# force the server to run on all interfaces, default is False (localhost)
RDS_ALL_INTERFACES = False

# set the debug mode, default is True - this means you can keep the main DEBUG
setting as False in the project's settings.py file
RDS_DEBUG = True
"""
from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Define our custom command."""

    help = "Runs the dev server with custom settings."

    def handle(self, *args, **options):
        """Handle the custom command."""
        # read the settings file
        dev_port = getattr(settings, "RDS_PORT", 8000)
        all_interfaces = getattr(settings, "RDS_ALL_INTERFACES", False)
        # use localhost unless RDS_ALL_INTERFACES is set
        dev_interface = "0.0.0.0" if all_interfaces else "127.0.0.1"

        # get the requested DEBUG setting and set this. If not specified then
        # default to TRUE since we are running dev settings.
        debug = getattr(settings, "RDS_DEBUG", True)
        settings.DEBUG = debug
        # print(settings.DEBUG)
        call_command("runserver", f"{dev_interface}:{dev_port}")
