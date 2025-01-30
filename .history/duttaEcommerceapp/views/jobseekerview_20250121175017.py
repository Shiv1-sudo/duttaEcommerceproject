from django.shortcuts import render, redirect
from django.http import JsonResponse  # Import JsonResponse
from django.views import View
from duttaEcommerceapp.models.jobseekermodel import JobSeekerUser, JobSeekerComment
from duttaEcommerceapp.forms.jobseekerform import JobSeekerUserForm  # Correct form reference
'''
def analyze_challenges(challenges):
    solutions = {
        'Intense Competition': ("Stand out with unique skills. Here's a guide: [Udemy](https://www.udemy.com/course/python-programming/)"),
        'Skill Gaps': ("Fill skill gaps with targeted courses. Try this one: [Coursera](https://www.coursera.org/specializations/python)"),
        'Networking Challenges': ("Join tech communities to expand your network: [Meetup](https://www.meetup.com/)"),
        'Automated Systems': ("Optimize your resume for ATS: [Jobscan](https://www.jobscan.co/)"),
        'Interview Stress': ("Prepare and practice with mock interviews: [Interview Cake](https://www.interviewcake.com/)"),
        'Economic Conditions': ("Explore remote job opportunities: [Remote OK](https://remoteok.io/)"),
        'Geographical Limitations': ("Consider remote work options: [We Work Remotely](https://weworkremotely.com/)"),
        'Personal Circumstances': ("Balance work and life: [LinkedIn Learning](https://www.linkedin.com/learning/)"),
        'Maintaining Motivation': ("Stay motivated with goal-setting: [Trello](https://trello.com/)"),
    }

    selected_challenges = challenges.split(', ')
    solution_texts = [solutions[challenge] for challenge in selected_challenges if challenge in solutions]
    return ', '.join(solution_texts)
'''
def analyze_challenges(challenges):
    solutions = {
        'Intense Competition': ("Stand out with unique skills. Here's a guide: <a href='https://www.udemy.com/course/python-programming/' target='_blank'>Udemy</a>"),
        'Skill Gaps': ("Fill skill gaps with targeted courses. Try this one: <a href='https://www.coursera.org/specializations/python' target='_blank'>Coursera</a>"),
        'Networking Challenges': ("Join tech communities to expand your network: <a href='https://www.meetup.com/' target='_blank'>Meetup</a>"),
        'Automated Systems': ("Optimize your resume for ATS: <a href='https://www.jobscan.co/' target='_blank'>Jobscan</a>"),
        'Interview Stress': ("Prepare and practice with mock interviews: <a href='https://www.interviewcake.com/' target='_blank'>Interview Cake</a>"),
        'Economic Conditions': ("Explore remote job opportunities: <a href='https://remoteok.io/' target='_blank'>Remote OK</a>"),
        'Geographical Limitations': ("Consider remote work options: <a href='https://weworkremotely.com/' target='_blank'>We Work Remotely</a>"),
        'Personal Circumstances': ("Balance work and life: <a href='https://www.linkedin.com/learning/' target='_blank'>LinkedIn Learning</a>"),
        'Maintaining Motivation': ("Stay motivated with goal-setting: <a href='https://trello.com/' target='_blank'>Trello</a>"),
    }

    selected_challenges = challenges.split(', ')
    solution_texts = [solutions[challenge] for challenge in selected_challenges if challenge in solutions]
    return ', '.join(solution_texts)

class JobSeeker(View):
    def get(self, request):
        form = JobSeekerUserForm()  # Correct form instance
        job_seeker_users = JobSeekerUser.objects.all()
        return render(request, 'job_seeker.html', {'form': form, 'job_seeker_users': job_seeker_users})

    def post(self, request):
        form = JobSeekerUserForm(request.POST)  # Correct form instance
        if form.is_valid():
            form.cleaned_data['challenges'] = ', '.join(form.cleaned_data['challenges'])
            form.cleaned_data['relax'] = analyze_challenges(form.cleaned_data['challenges'])
            job_seeker_user = JobSeekerUser.objects.create(**form.cleaned_data)

            response = {
                'relax': job_seeker_user.relax,
                'challenges': job_seeker_user.challenges,
                'achievements': job_seeker_user.achievements,
                'story': job_seeker_user.story,
                'created_at': job_seeker_user.created_at.strftime('%Y-%m-%d %H:%M:%S')
            }
            return JsonResponse(response)

        return JsonResponse({'error': 'Invalid form data'}, status=400)

def submit_comment(request, user_id):
    if request.method == 'POST':
        comment_text = request.POST.get('comment_text')
        job_seeker_user = JobSeekerUser.objects.get(id=user_id)
        JobSeekerComment.objects.create(job_seeker_user=job_seeker_user, comment_text=comment_text)
        return redirect('job_seekers')
