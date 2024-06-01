from django import forms
from rioz.models import Message, Information, About, Clients, Blog


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
        fields = '__all__'


class Blog_Form(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'