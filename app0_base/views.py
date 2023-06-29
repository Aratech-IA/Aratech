from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from Aratech_project.settings import EMAIL_CONTACT

from .forms import ContactForm


# Page Index
def index(request):
    return render(request, 'app0_base/index.html', {"index": True})


# Page Team
def team(request):
    return render(request, 'app0_base/team.html')


# Page Expertise
def expertise(request):
    return render(request, 'app0_base/expertise.html')


# Page Artificial intellignence
def ai(request):
    return render(request, 'app0_base/ai.html')


# Page Sérénicia
def serenicia(request):
    return render(request, 'app0_base/serenicia.html')


# Page contact
def contact(request):
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

            try:
                # Envoyer l'e-mail
                send_mail(
                    subject,
                    f'Prenom: {firstname} \n Nom: {name} \n Telephone: {phone} \n Email: {from_email} \n Sujet: {subject} \n Message: {message}',
                    from_email,
                    [EMAIL_CONTACT],
                )
                # Retourner un message de succès
                success_message = _("Your message has been sent successfully !")
                form = ContactForm()
                return render(request, 'app0_base/contact.html', {'form': form, 'success_message': success_message})

            except BadHeaderError:
                # En cas d'erreur de l'en-tête du message
                error_message = _("An error occurred while sending the message")
                return render(request, 'app0_base/contact.html', {'form': form, 'error_message': error_message})

            except OSError:
                # En cas d'erreur lors de l'envoie du message
                return render(request, 'app0_base/contact.html', {'form': form, 'error_message': error_message})

        # Retourner un message de succès
        #success_message = _("Your message has been sent successfully !")
        return render(request, 'app0_base/contact.html', {'form': form, 'error_message': error_message})

    else:
        form = ContactForm()

    return render(request, "app0_base/contact.html", {"form": form})


# Page Legal Notice
def legalnotice(request):
    return render(request, 'app0_base/legalnotice.html')
