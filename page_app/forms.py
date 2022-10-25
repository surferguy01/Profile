from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Name / Company', max_length=50, 
    widget=forms.TextInput(attrs={'placeholder':'Please enter your name'}))
  
    sender = forms.EmailField(label='Email',
    widget=forms.TextInput(attrs={'placeholder':'Please enter your email'}))
    
    subject = forms.CharField(max_length=70,
    widget=forms.TextInput(attrs={'placeholder':'Please enter a subject'}))
    
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Please offer me a job here..'}))
    