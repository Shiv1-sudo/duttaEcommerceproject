# views.py
from django.shortcuts import render
from duttaEcommerceapp.models.jobseekermodel import JobSeekerUser

def dashboard(request):
    # Retrieve all JobSeekerUser records
    job_seekers = JobSeekerUser.objects.all()

    # Data structures to hold the necessary information
    challenges_count = {}
    solutions_count = 0
    solution_links = set()

    for job_seeker in job_seekers:
        # Count challenges
        for challenge in job_seeker.challenges.split(', '):
            if challenge in challenges_count:
                challenges_count[challenge] += 1
            else:
                challenges_count[challenge] = 1

        # Count solutions and collect links
        if job_seeker.relax:
            solutions = job_seeker.relax.split(', ')
            solutions_count += len(solutions)
            solution_links.update(solutions)

    context = {
        'challenges_count': challenges_count,
        'solutions_count': solutions_count,
        'solution_links': solution_links,
    }

    return render(request, 'dashboard.html', context)
