

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from duttaEcommerceapp.models.gamemodel import Question, UserScore, GameResult

@login_required
def dsa_game(request):
    try:
        game_user = request.user
        score, created = UserScore.objects.get_or_create(game_user=game_user)

        # Reset the user's score at the start of a new game session
        score.score = 0
        score.save()

        # Clear previous game results
        GameResult.objects.filter(game_user=game_user).delete()

        questions = Question.objects.all()
        message_list = []

        # Process messages
        for message in messages.get_messages(request):
            message_list.append(str(message))

        return render(request, 'game/dsa_game.html', {'questions': questions, 'messages': message_list})
    except Exception as e:
        print(f"Error in dsa_game: {e}")
        messages.error(request, "An error occurred while loading the game.")
        return redirect('tech_connect')  # Redirect to a safe page in case of an error

@login_required
def submit_dsa_answer(request):
    try:
        if request.method == 'POST':
            game_user = request.user
            score, created = UserScore.objects.get_or_create(game_user=game_user)
            total_questions = Question.objects.count()
            correct_answers = 0

            for question in Question.objects.all():
                try:
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

                except Exception as e:
                    print(f"Error processing question {question.id}: {e}")
                    messages.error(request, f"An error occurred while processing question {question.id}.")

            score.last_played = timezone.now()
            score.save()

            # Add logic to display appropriate messages
            if correct_answers == total_questions:
                messages.success(request, 'Cleared level 1')
                messages.success(request, 'Congratulations!')  # Use success to ensure visibility
            elif correct_answers >= total_questions / 2:
                messages.info(request, 'Need to practice a bit more')
                messages.success(request, 'Well done!')  # Ensure both messages are visible

            return redirect('game_result')
        else:
            return redirect('dsa_game')  # Redirect GET requests to the DSA game page
    except Exception as e:
        print(f"Error in submit_dsa_answer: {e}")
        messages.error(request, "An error occurred while submitting your answers.")
        return redirect('dsa_game')  # Redirect to a safe page in case of an error

@login_required
def game_result(request):
    try:
        game_user = request.user
        score = UserScore.objects.get(game_user=game_user).score
        correct_answers = GameResult.objects.filter(game_user=game_user, correct=True).count()
        total_questions = Question.objects.count()

        return render(request, 'game/game_result.html', {
            'score': score,
            'correct_answers': correct_answers,
            'total_questions': total_questions
        })
    except Exception as e:
        print(f"Error in game_result: {e}")
        messages.error(request, "An error occurred while loading the game results.")
        return redirect('tech_connect')  # Redirect to a safe page in case of an error
