from django.http import JsonResponse
from django.shortcuts import render,redirect
from .models import *
from .forms import ApplicationForm,Branch


# Create your views here.
def home(request):
    return render(request, 'home.html')


def membership(request):
    if request.method == 'POST':
        # If the form has been submitted, process the data
        form = ApplicationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return render(request, 'succesmessage.html')
    else:
        # If the form hasn't been submitted, create a new form instance
        form = ApplicationForm()

    return render(request, 'membership.html',{'form': form})

def get_branches(request):
    district_id = request.GET.get('district')
    branches = Branch.objects.filter(district=district_id).values('id', 'name')

    # Convert QuerySet to dictionary
    branch_data = {branch['id']: branch['name'] for branch in branches}

    return JsonResponse({'branches': branch_data})
