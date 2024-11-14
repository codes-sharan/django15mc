from django import forms


class EmployeeForm(forms.Form):
    ename = forms.CharField()
    eaddr = forms.CharField()
    eno = forms.IntegerField()
    esal = forms.FloatField()

    