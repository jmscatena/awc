from django.shortcuts import render

from awc import company_data
from awc.company_data import get_training_programs
from cursos.models import Cursos


# Create your views here.
def courses(request):
    """Render the courses page"""
    #courses_data = Cursos.objects.filter(ativo=True)
    courses_data = company_data.get_courses()
    return render(request, 'courses.html', {'courses': courses_data})


def training(request):
    """Render the training programs page"""
    training_data = get_training_programs()
    return render(request, 'training.html', {'training_programs': training_data})
