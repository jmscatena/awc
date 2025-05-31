from django.shortcuts import render
import awc.company_data as company_data
# Create your views here.
def index(request):
    """Render the projects page with filterable gallery"""
    projects_data = company_data.get_projects()
    categories = sorted(set(project.get('empresa') for project in projects_data))
    filter_category = request.GET.get('category', '')

    if filter_category and filter_category != 'all':
        filtered_projects = projects_data.filter(empresa=filter_category)
    else:
        filtered_projects = projects_data

    return render(
        request,
        'projects.html',
        {
            'projects': filtered_projects,
            'categories': categories,
            'current_filter': filter_category
        }
    )
