from django.core.management.base import BaseCommand
from duttaEcommerceapp.models.gamemodel import UserScore

class Command(BaseCommand):
    help = 'Clear all user scores'

    def handle(self, *args, **kwargs):
        UserScore.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Cleared all user scores'))
