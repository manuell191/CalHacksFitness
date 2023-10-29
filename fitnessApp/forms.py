from django import forms
from .models import GOAL_BODY_TYPE

class LoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'autocomplete': 'off'
        })
    
    username = forms.CharField(label='Username', max_length=20, required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)

class SignupForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'autocomplete': 'off'
        })
    
    username = forms.CharField(label='Username', max_length=20, required=True)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)

class SetupForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(SetupForm, self).__init__(*args, **kwargs)
        #self.fields['username'].widget.attrs.update({
        #    'autocomplete': 'off'
        #})
    
    weight = forms.IntegerField(label='Weight (pounds)', required=True)
    height = forms.IntegerField(label='Height (inches)', required=True)
    goal = forms.ChoiceField(label='Goal', choices=GOAL_BODY_TYPE, required=True)
