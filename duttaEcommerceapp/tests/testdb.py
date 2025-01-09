from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Test the import of call_command'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Import successful'))
