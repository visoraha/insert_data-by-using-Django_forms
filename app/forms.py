from django import forms


class Student_form(forms.Form):
    sid=forms.IntegerField()
    name=forms.CharField(max_length=100)
    mbno=forms.IntegerField()
    email=forms.EmailField()