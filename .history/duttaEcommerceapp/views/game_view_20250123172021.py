
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
'''
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.http import JsonResponse
from duttaEcommerceapp.models.gamemodel import Question, UserScore, GameResult

@login_required
def dsa_game(request):
    questions = Question.objects.all()
    message_list = []

    # Process messages
    for message in messages.get_messages(request):
        message_list.append(str(message))

    return render(request, 'game/dsa_game.html', {'questions': questions, 'messages': message_list})

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
'''
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from duttaEcommerceapp.models.gamemodel import Question, UserScore, GameResult

@login_required
def dsa_game(request):
    questions = Question.objects.all()
    message_list = []

    # Process messages
    for message in messages.get_messages(request):
        message_list.append(str(message))

    return render(request, 'game/dsa_game.html', {'questions': questions, 'messages': message_list})

@login_required
def submit_dsa_answer(request):
    if request.method == 'POST':
        game_user = request.user
        score, created = UserScore.objects.get_or_create(game_user=game_user)
        total_questions = Question.objects.count()
        correct_answers = 0

        # Clear previous game results to avoid duplication
        GameResult.objects.filter(game_user=game_user).delete()

        for question in Question.objects.all():
            question_id = request.POST.get(f'question_id_{question.id}')
            selected_option = request.POST.get(f'option_{question.id}')

            # Check if selected_option is not None
            if not selected_option:
                messages.error(request, 'Please answer all questions before submitting.')
                return redirect('dsa_game')

            question = Question.objects.get(id=question_id)
            correct = selected_option == question.correct_option
            GameResult.objects.create(game_user=game_user, question=question, selected_option=selected_option, correct=correct)

            if correct:
                correct_answers += 1
                score.score += 50  # Assuming each question is worth 50 points
            else:
                score.score -= 25  # Assuming a penalty of 25 points for incorrect answers

        score.last_played = timezone.now()
        score.save()

        if correct_answers == total_questions:
            messages.success(request, 'Cleared level 1')
            messages.info(request, 'Congratulations!')
        elif correct_answers >= total_questions / 2:
            messages.info(request, 'Need to practice a bit more')
            messages.info(request, 'Well done!')

        return redirect('game_result')
    else:
        return redirect('dsa_game')  # Redirect GET requests to the DSA game page

@login_required
def game_result(request):
    game_user = request.user
    score = UserScore.objects.get(game_user=game_user).score
    correct_answers = GameResult.objects.filter(game_user=game_user, correct=True).count()
    total_questions = Question.objects.count()

    return render(request, 'game/game_result.html', {
        'score': score,
        'correct_answers': correct_answers,
        'total_questions': total_questions
    })
