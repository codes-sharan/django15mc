from django import forms
from django.core import validators


from firstapp.models import Employee

class EmployeeForm(forms.ModelForm):
    #code for validators
    class Meta:
        model = Employee
        fields = "__all__"
        widgets = {'ename': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Input your name here" })}
        labels = {'ename': "Employee Name"}




# class EmployeeForm(forms.Form):
#     ename = forms.CharField(label="Employee name: ")
#     eaddr = forms.CharField(label="Employee Address: ")
#     eno = forms.IntegerField(label="Employee Number: ")
#     esal = forms.FloatField(label="Employee Salary: ")
#     epass = forms.CharField(label="Employee Password", widget=forms.PasswordInput)
#     repass = forms.CharField(label="Reenter your password", widget=forms.PasswordInput)


#     def clean(self):
#         total_clean_data = super().clean()

#         fpass = total_clean_data["epass"]
#         spass = total_clean_data["repass"]

#         if fpass != spass:
#             raise forms.ValidationError("Both passwords must be same")




    # def clean(self):
    #     total_clean_data = super().clean()

    #     inputname = total_clean_data['ename']
    #     if inputname[0].lower() != 'v':
    #         raise forms.ValidationError("Name should start with v. ")
        
    #     inputaddr = total_clean_data['eaddr']
    #     if inputaddr != 'kathmandu':
    #         raise forms.ValidationError("Address should be kathmandu")



# def starts_with_v(value):
#     if value[0].lower() != 'v':
#         raise forms.ValidationError("Name should start with v")



# class EmployeeForm(forms.Form):
#     ename = forms.CharField(validators=[starts_with_v])
#     eaddr = forms.CharField()
#     eno = forms.IntegerField()
#     esal = forms.FloatField()

# class EmployeeForm(forms.Form):
#     ename = forms.CharField(validators=[validators.MaxLengthValidator(10), validators.MinLengthValidator(3)])
#     eaddr = forms.CharField()
#     eno = forms.IntegerField()
#     esal = forms.FloatField()


    # def clean_ename(self):
    #     inputname = self.cleaned_data['ename']
    #     if len(inputname) < 5:
    #         raise forms.ValidationError("The name should be > 5 characters")
    #     return inputname
    

    # def clean_eaddr(self):
    #     inputaddr = self.cleaned_data['eaddr']
    #     if inputaddr != "kathmandu":
    #         raise forms.ValidationError("Address should be kathmandu")
    #     return inputaddr
    
    # def clean_eno(self):
    #     inputno = self.cleaned_data['eno']
    #     if inputno < 1 :
    #         raise forms.ValidationError("Employee number should be positive")
    #     return inputno
    
    # def clean_esal(self):
    #     inputsal = self.cleaned_data['esal']
    #     if inputsal < 10000 or inputsal > 200000:
    #         raise forms.ValidationError("Employee salary should be in range 10,000-200,000")
    #     return inputsal


