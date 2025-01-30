from django.shortcuts import render, redirect
from django.views import View
from duttaEcommerceapp.models.jobseekermodel import JobSeekerUser
from duttaEcommerceapp.forms.jobseekerform import JobSeekerUserForm  # Correct form reference

class JobSeeker(View):
    def get(self, request):
        form = JobSeekerUserForm()  # Correct form instance
        job_seeker_users = JobSeekerUser.objects.all()
        return render(request, 'job_seeker.html', {'form': form, 'job_seeker_users': job_seeker_users})

    def post(self, request):
        form = JobSeekerUserForm(request.POST)  # Correct form instance
        if form.is_valid():
            form.save()
            return redirect('job_seekers')
        job_seeker_users = JobSeekerUser.objects.all()
        return render(request, 'job_seeker.html', {'form': form, 'job_seeker_users': job_seeker_users})
