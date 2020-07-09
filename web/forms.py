from django import forms
from django.contrib . auth.models import User
from web.models import UserProfileInfo

class UserInfo(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model=User
        fields = ('username','email','password')
    
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model=UserProfileInfo
        fields = ('portflio_site','profile_pic')