from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from projetos import views as projects_view
from cursos import views as courses_view
urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', projects_view.index, name='projects'),
    path('courses/', courses_view.courses, name='courses'),
    path('training/', courses_view.training, name='training'),
    path('publications/', views.publications, name='publications'),
    path('contact/', views.contact, name='contact'),
    path('subscribe-newsletter/', views.subscribe_newsletter, name='subscribe_newsletter'),
    path('admin/submissions/', views.admin_submissions, name='admin_submissions'),
    path('admin/subscriptions/', views.admin_subscriptions, name='admin_subscriptions'),
    path('admin/subscriptions/<int:subscription_id>/toggle/', views.toggle_subscription, name='toggle_subscription'),
]
#handler404 = 'views.page_not_found'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
