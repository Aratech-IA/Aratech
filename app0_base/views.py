"""views for app0_base"""

from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from django.conf import settings
import requests

from Aratech_project.settings import EMAIL_CONTACT

from .forms import ContactForm




# Page Index
def index(request):
    """index view"""
    return render(request, 'app0_base/index.html', {"index": True})


# Page Team
def team(request):
    """Team view"""
    return render(request, 'app0_base/team.html')


# Page Expertise
def expertise(request):
    """Expertise view"""
    return render(request, 'app0_base/expertise.html')


# Page Artificial intellignence
def ai(request):
    """AI view"""
    return render(request, 'app0_base/ai.html')


# Page Sérénicia
def serenicia(request):
    """Sérenicia view"""
    return render(request, 'app0_base/serenicia.html')


# Page contact
def contact(request):
    """Contact view"""
    error_message = _("Unable to send mail")
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            firstname = form.cleaned_data["firstname"]
            phone = form.cleaned_data["phone"]
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data["from_email"]
            message = form.cleaned_data['message']

            # reCAPTCHA verification
            recaptcha_token = request.POST.get('g-recaptcha-response')
            if not recaptcha_token:
                error_message = _('Invalid captcha')
                return render(request, 'app0_base/contact.html', {'form': form, 'error_message': error_message})

            url = 'https://www.google.com/recaptcha/api/siteverify'
            data = {
                'secret': settings.CAPTCHA_SECRETKEY,
                'response': recaptcha_token,
            }
            response = requests.post(url, data=data, timeout=5)

            if response.status_code == 200:
                json_response = response.json()
                if json_response['success']:
                    # Score de risque acceptable, traiter le formulaire
                    try:
                        # Envoyer l'e-mail
                        send_mail(
                            subject,
                            f'Nous avons reçu un message venant du formulaire contact de Aratech.fr : \n \n  Prenom : {firstname} \n  Nom : {name} \n  Telephone : {phone} \n  Email : {from_email} \n  Sujet : {subject} \n  Message : {message}',
                            "nicolas.lambert@aratech.fr",
                            [EMAIL_CONTACT],
                        )
                        # Retourner un message de succès
                        success_message = _("Your message has been sent successfully !")
                        form = ContactForm()
                        return render(request, 'app0_base/contact.html', {'form': form, 'success_message': success_message})
                    except BadHeaderError:
                        error_message = _("An error occurred while sending the message")
                    except OSError:
                        pass  # Handle other potential errors differently

                else:
                    # Score de risque suspect, refuser le formulaire
                    error_message = _('The reCAPTCHA indicates suspicious activity. Try Again...')
            else:
                # Erreur lors de la requête à l'API reCAPTCHA
                error_message = _('An error occurred while verifying the reCAPTCHA...')

            return render(request, 'app0_base/contact.html', {'form': form, 'error_message': error_message})

        else:
            form = ContactForm()

    else:
        form = ContactForm()

    return render(request, "app0_base/contact.html", {"form": form})


# Page Legal Notice
def legalnotice(request):
    """Legal Notice view"""
    return render(request, 'app0_base/legalnotice.html')
