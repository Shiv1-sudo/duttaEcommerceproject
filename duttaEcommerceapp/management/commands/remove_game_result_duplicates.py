from django.core.management.base import BaseCommand
from duttaEcommerceapp.models.gamemodel import GameResult

class Command(BaseCommand):
    help = 'Remove duplicate game results'

    def handle(self, *args, **kwargs):
        seen_results = set()
        duplicates = []

        for result in GameResult.objects.all():
            identifier = (result.game_user_id, result.question_id)
            if identifier in seen_results:
                duplicates.append(result.id)
            else:
                seen_results.add(identifier)

        if duplicates:
            GameResult.objects.filter(id__in=duplicates).delete()
            self.stdout.write(self.style.SUCCESS(f'Removed {len(duplicates)} duplicate game results'))
        else:
            self.stdout.write(self.style.SUCCESS('No duplicate game results found'))
