from django import forms
from contact.models import Contact
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = (
            'first_name', 'last_name', 'phone', 'email', 'description', 'category'
        )

    def clean(self):
        # cleaned_data = self.cleaned_data

        # self.add_error(
        #     'first_name',
        #     ValidationError(
        #         'Mensagem de erro',
        #         code='invalid'
        #     )
        # )

        return super().clean()
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if not first_name:
            raise ValidationError(
                'O campo first_name é obrigatorio.',
                code='invalid'
            )
        if any(char.isdigit() for char in first_name):
            raise  ValidationError(
                'Deve ser um nome valido.',
                code='invalid'
            )
        return first_name
    
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')

        if not last_name:
            raise ValidationError(
                'O campo last_name é obrigatorio.',
                code='invalid'
            )
        if any(char.isdigit() for char in last_name):
            raise  ValidationError(
                'Deve ser um nome valido.',
                code='invalid'
            )
        return last_name
    

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        required=True
    )
    last_name = forms.CharField(
        required=True
    )
    email = forms.EmailField()

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username', 'password1', 'password2',
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError('Esse email já existe.', code='invalid')
            )

        return email