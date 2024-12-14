from django import forms
from.models import Student, Address, Teacher

class StudentForm(forms.ModelForm):
    class Meta :
        model = Student
        fields = ['name', 'age', 'address']

    name  = forms.CharField(max_length=40, widget = forms.TextInput())
    age = forms.IntegerField(min_value= 0, widget=forms.NumberInput())
    address = forms.ModelChoiceField(queryset=Address.objects.all(), widget= forms.Select())



class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'photo']

    name = forms.CharField(max_length=20, widget= forms.TextInput())
    photo = forms.ImageField(widget= forms.ClearableFileInput())