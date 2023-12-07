from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import*

class SignInForm(AuthenticationForm):
    username = forms.CharField(widget = forms.TextInput(attrs = {
        'class': 'w-full py-4 px-6 rounded-xl',
    }))
    password = forms.CharField(widget = forms.PasswordInput(attrs = {
        'class': 'w-full py-4 px-6 rounded-xl',
    }))

class SignUpForm(UserCreationForm):
    class Meta():
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    username = forms.CharField(widget = forms.TextInput(attrs = {
        'class': 'w-full py-4 px-6 rounded-xl',
    }))
    email = forms.CharField(widget = forms.EmailInput(attrs = {
        'class': 'w-full py-4 px-6 rounded-xl',
    }))
    password1 = forms.CharField(widget = forms.PasswordInput(attrs = {
        'class': 'w-full py-4 px-6 rounded-xl',
    }))
    password2 = forms.CharField(widget = forms.PasswordInput(attrs = {
        'class': 'w-full py-4 px-6 rounded-xl',
    }))

class PostUploadForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ['title', 'content', 'headerImg']

    title = forms.CharField(widget = forms.TextInput(attrs = {
        'class': 'w-full py-4 px-6 rounded-xl',
    }))
    content = forms.CharField(widget = forms.Textarea(attrs = {
        'class': 'w-full py-4 px-6 rounded-xl',
    }))

class PostUpdateForm(forms.Form):
    title = forms.CharField(max_length = 116, widget = forms.TextInput(attrs = {
        'class': 'w-full py-4 px-6 rounded-xl',
    }))
    content = forms.CharField(widget = forms.Textarea(attrs = {
        'class': 'w-full py-4 px-6 rounded-xl',
    }))
    headerImg = forms.ImageField(required = False, allow_empty_file = True)

class ProfileUpdateForm(forms.Form):
    image = forms.ImageField(required = False, allow_empty_file = True)
    description = forms.CharField(widget = forms.Textarea(attrs = {
        'class': 'w-full py-4 px-6 rounded-xl',
    }))

class CommentPostForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ['content']

    content = forms.CharField(widget = forms.Textarea(attrs = {
        'class': 'w-full py-4 px-6 rounded-xl border-gray-200 border',
    }))