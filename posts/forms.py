from django import forms


class PostForm(forms.ModelForm):
    image = forms.ImageField()
    title = forms.CharField()
    content = forms.CharField()
