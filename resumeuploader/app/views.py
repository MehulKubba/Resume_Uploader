from django.shortcuts import render, redirect
from .forms import ResumeForm
from .models import Resume
from django.views import View

class HomeView(View):
    def get(self, request):
        form = ResumeForm()
        candidates = Resume.objects.all()
        return render(request, 'app/home.html', {'candidates': candidates, 'form': form})

    def post(self, request):
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirect to avoid form resubmission on refresh
            return redirect('home')  # Assuming 'home' is the name of the URL pattern for HomeView
        # If form is not valid, render the same template with the form
        return render(request, 'app/home.html', {'form': form})

class CandidateView(View):
    def get(self, request, pk):
        candidate = Resume.objects.get(pk=pk)
        return render(request, 'app/candidate.html', {'candidate': candidate})
