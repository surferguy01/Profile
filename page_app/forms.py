from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField(required=True)
    subject = forms.CharField(max_length=70)
    message = forms.CharField(widget=forms.Textarea)