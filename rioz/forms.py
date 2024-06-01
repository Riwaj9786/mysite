from django import forms
from rioz.models import Message, Information, About, Comments, Clients, Blog


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('name', 'email', 'message')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }


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



class Comment_Form(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment_name', 'comment_text']

    def __init__(self, *args, **kwargs):
        super(Comment_Form, self).__init__(*args, **kwargs)
        self.fields['comment_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['comment_text'].widget.attrs.update({'class': 'form-control'})