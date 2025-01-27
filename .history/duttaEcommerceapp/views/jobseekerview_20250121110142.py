from django.shortcuts import render,redirect
from django.views import View
from duttaEcommerceapp.models.jobseekermodel import User
from duttaEcommerceapp.forms.jobseekerform import UserForm


'''
# views.py
from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm
class JobSeeker(View):
    def get(self, request):
        print(f"Requested URL: {request.build_absolute_uri()}")
        return render(request, 'job_seeker.html')

def job_seekers(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('job_seekers')
    else:
        form = UserForm()
    users = User.objects.all()
    return render(request, 'job_seekers.html', {'form': form, 'users': users})

'''