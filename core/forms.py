#-*- coding: utf-8 -*-
from django import forms
from models import Link
from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext as _

class UserCreationForm(forms.Form):
    """
    UserForm - Form to create a new user
    """
    error_messages = {
        'password_match': _(u'Confirmar senha não confere com a senha informada!'),
        'name_exist' 	: _(u'O nome já existe, tente outro!'),
        'email_exist' 	: _(u'O email já existe, tente outro!'),
    }

    help_messages = {
        'confirm_pass' : _(u'Informe a mesma senha como acima, para verificação.'),
    }

    name  = forms.CharField(label=_('Nome'), widget=forms.TextInput, required=True, initial='')
    email = forms.EmailField(label=_('Email'), widget=forms.EmailInput, required=True, initial='')
    password = forms.CharField(label=_('Senha'), widget=forms.PasswordInput, required=True, initial='')

    confirm_password = forms.CharField(
        label=_('Confirmar Senha'),
        widget=forms.PasswordInput,
        required=True,
        help_text=help_messages['confirm_pass'],
        initial=''
    )

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.user = get_user_model()

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

class AuthenticationForm(forms.Form):
    """
    AuthenticationForm - Form to auth an user
    """
    error_messages = {
        'invalid_login' : u'Usuário ou Senha inválido. Tente novamente!',
    }

    email    = forms.EmailField(label=_('Email'), widget=forms.EmailInput, required=True, initial='')
    password = forms.CharField(label=_('Senha'), widget=forms.PasswordInput, required=True, initial='')

    def __init__(self, *args, **kwargs):
        super(AuthenticationForm, self).__init__(*args, **kwargs)
        self.user = None

    def clean(self):
        email    = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:

            self.user = authenticate(email=email, password=password)

            if self.user is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'],
                    code='invalid_login'
                )

        return self.cleaned_data

    def get_user(self):
        return self.user

class LinkForm(forms.ModelForm):
    """
    LinkForm - Form to create a new shortened url
    """
    class Meta:
        model  = Link
        fields = ('url', )