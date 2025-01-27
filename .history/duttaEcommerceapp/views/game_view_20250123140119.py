from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from duttaEcommerceapp.models.gamemodel import Question, UserScore
from django.utils import timezone

@login_required
def home(request):
    questions = Question.objects.all()
    return render(request, 'game/home.html', {'questions': questions})

@login_required
def submit_answer(request):
    if request.method == 'POST':
        user = request.user
        score, created = UserScore.objects.get_or_create(user=user)
        question_id = request.POST.get('question_id')
        selected_option = request.POST.get('option')
        question = Question.objects.get(id=question_id)

        if selected_option == question.correct_option:
            score.score += 10
        else:
            score.score -= 5

        score.last_played = timezone.now()
        score.save()
        return redirect('home')
