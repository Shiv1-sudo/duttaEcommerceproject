from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError

class Command(BaseCommand):
    help = 'Checks if the database is connected.'

    def handle(self, *args, **kwargs):
        print("Executing 'check_db' command")
        db_conn = connections['default']
        try:
            db_conn.cursor()
            self.stdout.write(self.style.SUCCESS('Database connection successful.'))
        except OperationalError:
            self.stdout.write(self.style.ERROR('Database connection failed.'))
