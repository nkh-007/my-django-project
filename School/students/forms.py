from django import forms
from .models import Stud

class StudForm(forms.ModelForm):
    class Meta:
        model = Stud #table
        fields = ['roll_number', 'stud_name','father_name','email','math','english','history','science','hindi']
        