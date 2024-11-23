from django import forms 
from .models import CustomUser 

class CustomUserCreationForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput, label='Password')
    password_confirm=forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

    class Meta:
        model=CustomUser
        fields=['username', 'nickname', 'email', 'image', 'phone_num', 'birthday', 'address']

    def clean(self): 
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password != password_confirm:
            self.add_error('password_confirm', "Passwords do not match")
             
        return cleaned_data
    
class CustomUserLoginForm(forms.Form):
    username = forms.CharField(max_length=150, label='Username')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')