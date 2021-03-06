from django import forms
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm , UsernameField
from django.contrib.auth.models import User
from django.forms.widgets import Widget
from django.utils.translation import gettext, gettext_lazy as _



from .models import  PhotoGallary

class ImageForm(forms.ModelForm):
    class Meta:
        model = PhotoGallary
        fields=['multipleimages','desc']  
        label ={}
        widgets ={
            'multipleimages':forms.FileInput(attrs={'id':'myfile','class':'form-control-file','multiple':True}),
            'desc':forms.Textarea(attrs={'class':'form-control'}),
        } 


class SignUpForm(UserCreationForm):
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Password(again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'email':'Email'}
        widgets={'username':forms.TextInput(attrs={'class':'form-control'}),
                'first_name':forms.TextInput(attrs={'class':'form-control'}),
                'last_name':forms.TextInput(attrs={'class':'form-control'}),
                'email':forms.EmailInput(attrs={'class':'form-control'}),
                
                
                }
        

class LoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))    
    password=forms.CharField(label= _("Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))
    



