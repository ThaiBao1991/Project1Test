from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
 
class createuserform(UserCreationForm):
    class Meta:
        model=User
        fields=['username']  # Mặc định sẽ thêm vào password và Password Confirmation
        # fields=['username','password'] 
        # fields='__all__'
 
class createcustomerform(ModelForm):
    class Meta:
        model=Customer
        fields='__all__'
        exclude=['user']
 
class createbookform(ModelForm):
    class Meta:
        model=Book
        fields='__all__'