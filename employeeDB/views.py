from django.shortcuts import render, redirect
from .models import EmployeeDB
from .forms import EmployeeForm

# Create your views here.


def emp_list(request):
    employeeList = EmployeeDB.objects.all().order_by('employeeID')
    return render (request, 'home.html', {'emp_list': employeeList})

def emp_form(request,id=0):
    if request.method == 'GET':
        if id == 0:
            form = EmployeeForm()
        else:
            employee = EmployeeDB.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render (request, 'emp_form.html', {'form':form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = EmployeeDB.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance = employee) 
        if form.is_valid():
            form.save()
        return redirect('/')

def emp_delete(request,id):
    employee = EmployeeDB.objects.get(pk=id)
    employee.delete()
    return redirect("/")
