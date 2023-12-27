from django import forms
from django.contrib.auth import authenticate,login,get_user_model
class registrationform(forms.Form):

    firstname=forms.CharField()
    lastname=forms.CharField()
    username=forms.CharField()

    email = forms.EmailField()
    password=forms.CharField()
    password2=forms.CharField(label='confirm password')

    def clean(self):
        data=self.cleaned_data
        password=self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password2 !=password:
            raise forms.ValidationError('password not match')
        return data
    def clean_username(self):
        username=self.cleaned_data.get('username')
        qs=user.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError('Username is already taken')
        return username

    def clean_email(self):
        email=self.cleaned_data.get('email')
        qs=user.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('email already exists')