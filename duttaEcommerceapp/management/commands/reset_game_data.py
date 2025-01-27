from django.core.management.base import BaseCommand
from duttaEcommerceapp.models.gamemodel import GameResult, UserScore

class Command(BaseCommand):
    help = 'Reset game data'

    def handle(self, *args, **kwargs):
        GameResult.objects.all().delete()
        UserScore.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully reset game data'))
