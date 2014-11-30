#coding:utf-8
from django import forms
from models import User
from django.utils.translation import ugettext as _

class UserCreationForm(forms.Form):

    error_messages = {
        'password_match': _(u'The password does not match...'),
        'name_exist' 	: _(u'The name already exists, try another!'),
        'email_exist' 	: _(u'The email already exists, try another!'),
    }

    help_messages = {
        'confirm_pass' : _(u'Informe a mesma senha como acima, para verificação.'),
    }

    name  = forms.CharField(label=_('Name'), widget=forms.TextInput, required=True, initial='')
    email = forms.EmailField(label=_('Email'), widget=forms.TextInput, required=True, initial='')
    password = forms.CharField(label=_('Password'), widget=forms.PasswordInput, required=True, initial='')

    confirm_password = forms.CharField(
        label=_('Confirm Password'),
        widget=forms.PasswordInput,
        required=True,
        help_text=help_messages['confirm_pass'],
        initial=''
    )

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.user = User

    def clean_name(self):
        name = self.cleaned_data.get('name')
        try:
            self.user.objects.get(name=name)
        except self.user.DoesNotExist:
            return name

        raise forms.ValidationError(
            self.error_messages['name_exist'],
            code='name_exist'
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            self.user.objects.get(email=email)
        except self.user.DoesNotExist:
            return email
        raise forms.ValidationError(
            self.error_messages['email_exist'],
            code='email_exist'
        )

    def clean_confirm_password(self):
        password 		 = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError(self.error_messages['password_match'], code='password_match')
        return confirm_password


