from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control rounded-pill mb-2 mb-md-4'}))
    firstname = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control rounded-pill mb-2 mb-md-4'}))
    phone = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control rounded-pill mb-2 mb-md-4'}))
    from_email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control rounded-pill mb-2 mb-md-4'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control rounded-4'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control rounded-4'}), required=True)
