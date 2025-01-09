'''import webbrowser
import time
from django.conf import settings
from django.core.management.commands.runserver import Command as RunserverCommand

class Command(RunserverCommand):
    def inner_run(self, *args, **options):
        super().inner_run(*args, **options)
        webbrowser.open(settings.BASE_URL)
        time.sleep(10)  # Wait for 10 seconds'''

import os
import webbrowser
import threading
from django.core.management.commands.runserver import Command as RunserverCommand

def open_browser():
    webbrowser.open_new('http://127.0.0.1:8000')

class Command(RunserverCommand):
    def handle(self, *args, **options):
        if options['use_threading']:
            threading.Timer(1.25, open_browser).start()
        super().handle(*args, **options)
       
