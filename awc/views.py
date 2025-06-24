from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from . import company_data
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

def index(request):
    """Render the home page with company overview"""
    company_info = company_data.get_company_info()
    #featured_projects = Projetos.objects.filter(ativo=True)[:3]
    #featured_courses = Cursos.objects.filter(ativo=True)[:2]
    featured_projects = company_data.get_projects()[:3]
    featured_courses = company_data.get_courses()[:2]
    return render(
        request,
        'index.html',
        {
            'company_info': company_info,
            'featured_projects': featured_projects,
            'featured_courses': featured_courses
        }
    )
def admin_submissions(request):
    """View all contact form submissions"""
    submissions = company_data.ContactSubmission.objects.order_by('-created_at')
    return render(request, 'admin/submissions.html', {'submissions': submissions})


def admin_subscriptions(request):
    """View all newsletter subscriptions"""
    subscriptions = company_data.NewsletterSubscription.objects.order_by('-subscribed_at')
    return render(request, 'admin/subscriptions.html', {'subscriptions': subscriptions})


def toggle_subscription(request, subscription_id):
    """Toggle active status of a newsletter subscription"""
    if request.method == 'POST':
        subscription = get_object_or_404(company_data.NewsletterSubscription, pk=subscription_id)
        subscription.is_active = not subscription.is_active
        try:
            subscription.save()
            if subscription.is_active:
                messages.success(request, f"Subscription for {subscription.email} has been activated.")
            else:
                messages.success(request, f"Subscription for {subscription.email} has been deactivated.")
        except Exception as e:
            messages.error(request, "An error occurred while updating the subscription status.")
        return redirect('admin_subscriptions')
    return None


def page_not_found(request, exception):
    """Custom 404 error page"""
    return render(request, '404.html', status=404)

def publications(request):
    """Render the publications page with downloadable resources"""
    publications_data = company_data.get_publications()
    return render(request, 'publications.html', {'publications': publications_data})


def contact(request):
    """Handle contact form submission"""
    if request.method == 'POST':
        form = company_data.ContactForm(request.POST)
        if form.is_valid():
            try:
                # --- CORRIGIDO: Removidas as vírgulas do final ---
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                subject = form.cleaned_data['subject']
                inquiry_type = form.cleaned_data['inquiry_type']
                message = form.cleaned_data['message']

                plain_message = (
                    f"Você recebeu uma nova mensagem de contato:\n\n"
                    f"Nome: {name}\n"
                    f"E-mail: {email}\n"
                    f"Categoria: {inquiry_type}\n"
                    f"Assunto: {subject}\n\n"
                    f"Mensagem:\n{message}"
                )

                # Usando as variáveis subject e plain_message no envio
                send_mail(
                    f"Novo Contato via Site: {subject}",  # Assunto dinâmico
                    plain_message,  # Corpo do e-mail
                    settings.EMAIL_HOST_USER,  # Remetente configurado
                    ['info@awc.tec.br'],  # Destinatário
                    fail_silently=False
                )
                messages.success(request, 'Thank you for your message! We will get back to you soon.')
                return redirect('contact')

            except Exception as e:
                # Bloco de exceção melhorado para depuração
                print(f"ERRO AO PROCESSAR FORMULÁRIO DE CONTATO: {e}")
                messages.error(request, 'An error occurred while sending your message. Please try again later.')
                # Não redirecione aqui, para que o usuário não perca os dados digitados
    else:
        form = company_data.ContactForm()

    # O return final renderiza o formulário (novo ou com erros)
    return render(request, 'contact.html', {'form': form})

def subscribe_newsletter(request):
    """Handle newsletter subscription form"""
    if request.method == 'POST':
        email = request.POST.get('email')
        if not email:
            messages.error(request, 'Email is required for subscription')
            return redirect(request.META.get('HTTP_REFERER', 'index'))

        existing_subscription = company_data.NewsletterSubscription.objects.filter(email=email).first()

        if existing_subscription:
            if existing_subscription.is_active:
                messages.info(request, 'You are already subscribed to our newsletter!')
            else:
                existing_subscription.is_active = True
                existing_subscription.save()
                messages.success(request, 'Your subscription has been reactivated!')
        else:
            try:
                company_data.NewsletterSubscription.objects.create(
                    email=email,
                    first_name=request.POST.get('first_name', '')
                )
                messages.success(request, 'Thank you for subscribing to our newsletter!')
            except Exception as e:
                messages.error(request, 'An error occurred while processing your subscription.')

        return redirect(request.META.get('HTTP_REFERER', 'index'))
    return None


