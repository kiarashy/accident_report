from django.shortcuts import render, redirect, get_object_or_404
from django.db import models
from rest_framework import generics
from .models import AccidentReport
from .serializers import AccidentReportSerializer
from .forms import AccidentReportForm
from django.http import JsonResponse
from django.db.models import Q





class AccidentReportListCreateView(generics.ListCreateAPIView):
    queryset = AccidentReport.objects.all()
    serializer_class = AccidentReportSerializer


def home_view(request):
    return render(request, 'home.html')  # This will render the homepage template


def accident_report_view(request):
    if request.method == "POST":
        form = AccidentReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reports:success')   # Redirect after successful form submission
    else:
        form = AccidentReportForm()

    return render(request, 'report_form.html', {'form': form})

def success_view(request):
    return render(request, 'home.html')



def accident_list(request):
    query = request.GET.get('q', '')
    spam_type = request.GET.get('spam_type', '')
    siren = request.GET.get('siren', '')
    email = request.GET.get('email', '')
    name = request.GET.get('name', '')

    accidents = AccidentReport.objects.all()

    if query:
        accidents = accidents.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(location__icontains=query)
        )

    if spam_type:
        accidents = accidents.filter(spam_type__icontains=spam_type)

    if siren:
        accidents = accidents.filter(siren__icontains=siren)

    if email:
        accidents = accidents.filter(
            Q(spam_email__icontains=email) |
            Q(vic_email__icontains=email)
        )

    if name:
        accidents = accidents.filter(spam_name__icontains=name)

    # Sort by votes first
    accidents = accidents.order_by('-vote_count', '-created_at')

    return render(request, 'reports/accident_list.html', {
        'accidents': accidents,
        'query': query,
        'spam_type': spam_type,
        'siren': siren,
        'email': email,
        'name': name,
    })




def upvote_report(request, report_id):
    report = get_object_or_404(AccidentReport, id=report_id)
    report.vote_count += 1  # Increase the vote count
    report.save()
    
    # If AJAX request, return JSON response
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'new_vote_count': report.vote_count})

    return redirect('accident_list')  # Redirect to the list if not using AJAX