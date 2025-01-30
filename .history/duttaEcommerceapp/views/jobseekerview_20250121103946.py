from django.shortcuts import render
from django.views import View

class JobSeeker(View):
    def get(self, request):
        print(f"Requested URL: {request.build_absolute_uri()}")
        return render(request, 'job_seeker.html')
