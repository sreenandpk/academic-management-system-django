from django.shortcuts import render, get_object_or_404
from .models import Subject

def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, "subjects/subject_list.html", {"subjects": subjects})

def subject_detail(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    return render(request, "subjects/subject_detail.html", {"subject": subject})