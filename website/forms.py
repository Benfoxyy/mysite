from django import forms
from .models import contact,Newsletter
from captcha.fields import CaptchaField

#class myforms(forms.Form):
#    name = forms.CharField(max_length=255)
#    email = forms.EmailField()
#    subject = forms.CharField(max_length=255)
#    message = forms.CharField(widget=forms.Textarea)

class ContactForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = contact
        fields = '__all__'

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email']