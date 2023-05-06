from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
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
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            firstname = form.cleaned_data["firstname"]
            phone = form.cleaned_data["phone"]
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data["from_email"]
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ["contact@aratech.fr"])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("success")
    return render(request, "app0_base/contact.html", {"form": form})


# A rajouter dans les urls
def success(request):
    return HttpResponse("Success ! Thank you for your message.")


# Page Legal Notice
def legalnotice(request):
    return render(request, 'app0_base/legalnotice.html')
