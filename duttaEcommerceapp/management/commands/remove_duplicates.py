from django.core.management.base import BaseCommand
from duttaEcommerceapp.models.gamemodel import Question

class Command(BaseCommand):
    help = 'Remove duplicate questions'

    def handle(self, *args, **kwargs):
        seen_questions = set()
        duplicates = []

        for question in Question.objects.all():
            if question.question_text in seen_questions:
                duplicates.append(question.id)
            else:
                seen_questions.add(question.question_text)

        if duplicates:
            Question.objects.filter(id__in=duplicates).delete()
            self.stdout.write(self.style.SUCCESS(f'Removed {len(duplicates)} duplicate questions'))
        else:
            self.stdout.write(self.style.SUCCESS('No duplicate questions found'))
