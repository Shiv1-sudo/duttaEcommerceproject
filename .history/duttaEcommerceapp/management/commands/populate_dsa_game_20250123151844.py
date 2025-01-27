  # Ensure the import path is correct
'''
from django.core.management.base import BaseCommand
from duttaEcommerceapp.models.gamemodel import Question
class Command(BaseCommand):
    help = 'Populate the database with initial DSA questions'

    def handle(self, *args, **kwargs):
        questions_data = [
            {
                "question_text": "What is the time complexity of binary search?",
                "option1": "O(n)",
                "option2": "O(log n)",
                "option3": "O(n log n)",
                "option4": "O(n^2)",
                "correct_option": "O(log n)",
                "explanation": "Binary search works by dividing the search interval in half repeatedly, leading to a logarithmic time complexity."
            },
            {
                "question_text": "Which data structure is used in Breadth-First Search?",
                "option1": "Stack",
                "option2": "Queue",
                "option3": "Heap",
                "option4": "Tree",
                "correct_option": "Queue",
                "explanation": "Breadth-First Search uses a queue to explore nodes level by level."
            },
            # Add more questions here...
        ]

        for question_data in questions_data:
            Question.objects.create(**question_data)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with DSA questions'))
'''
from django.core.management.base import BaseCommand
from duttaEcommerceapp.models.gamemodel import Question

class Command(BaseCommand):
    help = 'Populate the database with initial DSA questions'

    def handle(self, *args, **kwargs):
        questions_data = [
            {
                "question_text": "What is the time complexity of binary search?",
                "option1": "O(n)",
                "option2": "O(log n)",
                "option3": "O(n log n)",
                "option4": "O(n^2)",
                "correct_option": "O(log n)",
                "explanation": "Binary search works by dividing the search interval in half repeatedly, leading to a logarithmic time complexity."
            },
            {
                "question_text": "Which data structure is used in Breadth-First Search?",
                "option1": "Stack",
                "option2": "Queue",
                "option3": "Heap",
                "option4": "Tree",
                "correct_option": "Queue",
                "explanation": "Breadth-First Search uses a queue to explore nodes level by level."
            },
            # Add more questions here...
        ]

        for question_data in questions_data:
            Question.objects.create(**question_data)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with DSA questions'))
