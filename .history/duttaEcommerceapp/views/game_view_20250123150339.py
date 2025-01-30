from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from duttaEcommerceapp.models.gamemodel import Question, UserScore, GameResult
from django.contrib import messages
from django.utils import timezone
'''
@login_required
def dsa_game(request):
    questions = Question.objects.all()
    return render(request, 'game/dsa_game.html', {'questions': questions})

@login_required
def submit_dsa_answer(request):
    if request.method == 'POST':
        game_user = request.user  # Updated variable name
        score, created = UserScore.objects.get_or_create(game_user=game_user)  # Updated field name
        question_id = request.POST.get('question_id')
        selected_option = request.POST.get('option')
        question = Question.objects.get(id=question_id)

        if selected_option == question.correct_option:
            score.score += 10
        else:
            score.score -= 5

        score.last_played = timezone.now()
        score.save()
        return redirect('dsa_game')
'''


@login_required
def dsa_game(request):
    questions = Question.objects.all()
    return render(request, 'game/dsa_game.html', {'questions': questions})

@login_required
def submit_dsa_answer(request):
    if request.method == 'POST':
        game_user = request.user
        score, created = UserScore.objects.get_or_create(game_user=game_user)
        question_id = request.POST.get('question_id')
        selected_option = request.POST.get('option')
        question = Question.objects.get(id=question_id)

        correct = selected_option == question.correct_option
        GameResult.objects.create(game_user=game_user, question=question, selected_option=selected_option, correct=correct)

        if correct:
            score.score += 10
        else:
            score.score -= 5

        score.last_played = timezone.now()
        score.save()

        # Calculate results
        total_questions = GameResult.objects.filter(game_user=game_user).count()
        correct_answers = GameResult.objects.filter(game_user=game_user, correct=True).count()

        if correct_answers == total_questions:
            messages.success(request, 'Cleared level 1')
            messages.info(request, 'Congratulations!')
        elif correct_answers >= total_questions / 2:
            messages.info(request, 'Need to practice a bit more')
            messages.info(request, 'Well done!')

        return redirect('dsa_game')
