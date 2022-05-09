from django.shortcuts import redirect, render
from employe.models import Employee
from employe.forms import EmployeeForm
from django.contrib import messages


# Create your views here.


def Emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Successfully Added")
                return redirect("/show")
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, 'index.html', {'form': form})


def show(request):
    employee = Employee.objects.all()
    return render(request, 'show.html', {'employee': employee})


def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, 'edit.html', {'employee': employee})


def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance=employee)
    if form.is_valid():
        form.save()
        return redirect("/show")
    else:
        form = EmployeeForm()
    return render(request, 'edit.html', {'form': form})


def delete(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/show")
