from django.shortcuts import render
from firstapp.models import Employee
from . import forms

# Create your views here.
def index(request):
    my_obj = Employee.objects.all()
    context = {"my_obj": my_obj}
    return render(request, 'firstapp/index.html', context = context)


def formIndex(request):
    form = forms.EmployeeForm()
    if request.method == "POST":
        form = forms.EmployeeForm(request.POST)
        if form.is_valid():
            #print("Name: ",form.cleaned_data["ename"] )
            form.save(commit=True)

            # Employee.objects.create(ename=form.cleaned_data['ename'], eno=form.cleaned_data['eno'], esal=form.cleaned_data['esal'], eaddr=form.cleaned_data['eaddr'])
            
        form = forms.EmployeeForm()

    context = {"form": form}
    return render(request, "firstapp/employeerecord.html", context=context)


