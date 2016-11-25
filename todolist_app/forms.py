from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from todolist_app.models import Task


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Email', 'class': 'signupfield'}))
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'First Name', 'class': 'signupfield'}))
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Last Name', 'class': 'signupfield'}))
    username = forms.CharField(widget=forms.widgets.TextInput(attrs={'placeholder': 'Username', 'class': 'signupfield'}))
    password1 = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password', 'class': 'signupfield'}))
    password2 = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password Confirmation', 'class': 'signupfield'}))

    class Meta:
        fields = ['username', 'first_name', 'last_name', 'email', 'password1',
                  'password2']
        model = User

# class ImageUploadForm(forms.Form):
#     image = forms.ImageField()

class AuthenticateForm(AuthenticationForm):
    username = forms.CharField(widget=forms.widgets.TextInput(attrs={'placeholder': 'Username', 'class': 'login-field'}))
    password = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password', 'class': 'login-field'}))


class TaskBox(forms.ModelForm):
    task_text = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Write your wish...',
                                                                                     'class': 'task-box'}))

    class Meta:
        model = Task
        exclude = ('user', 'rank', 'creation_date')
