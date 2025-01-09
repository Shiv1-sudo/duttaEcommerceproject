from django.shortcuts import render
from django.views import View

class HomePageView(View):
    def get(self, request):
        print(f"Requested URL: {request.build_absolute_uri()}")
        return render(request, 'home.html')
