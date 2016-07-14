from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, label='Assunto')
    message = forms.CharField(widget=forms.Textarea, label='Mensagem')
    sender = forms.EmailField(label='Email')
    cc_myself = forms.BooleanField(required=False, label='Me Copiar')
