from django.shortcuts import render
import awc.company_data as company_data
# Create your views here.
def inovations(request):
    """Render the courses page"""
    courses_data = company_data.Cursos.objects.filter(ativo=True)
    return render(request, 'courses.html', {'courses': courses_data})
