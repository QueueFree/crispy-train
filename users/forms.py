from django import forms
from django.forms import EmailField

from posts.models import Tag


class RegisterForm(forms.Form):
    username = forms.CharField()
    email = EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    password = forms.CharField()
    password_confirm = forms.CharField()

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Passwords do not match')

        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


class SearchForm(forms.Form):
    search = forms.CharField(
        required=False,
        max_length=149,
        widget=forms.TextInput(
            attrs={
                "placeholder": "введите текст для поиска",
                "class": "form-control",
            }),
    )
    tag = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
    )
    orderings = (
        {"title", "Искать по названию"},
        {"-title", "В обратном порядке"},
        {"rate", "По рейтингу"},
        {"-rate", "Худшие Посты"},
        {"created_at", "По дате создания"}
    )

    ordering = forms.ChoiceField(
        required=False,
        choices=orderings,
        widget=forms.Select(attrs={"class": "form-control"}),
    )
