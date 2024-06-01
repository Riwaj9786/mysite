from django import forms
<<<<<<< HEAD
from rioz.models import Message, Information, About, Clients, Blog
=======
from rioz.models import Message, Information, About, Clients
>>>>>>> origin/main

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('name', 'email', 'message')


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Information
        fields = ('cv',)


class Info_EditForm(forms.ModelForm):
    class Meta:
        model = Information
        fields = ('name', 'avatar', 'address', 'email', 'contact', 'born_date')


class About_EditForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ('short_bio', 'intro')


class Client_Form(forms.ModelForm):
    class Meta:
        model = Clients
<<<<<<< HEAD
        fields = '__all__'


class Blog_Form(forms.ModelForm):
    class Meta:
        model = Blog
=======
>>>>>>> origin/main
        fields = '__all__'