# from django.shortcuts import rende
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import emp

# Create your views here.
def employee_home(request):

    emps = emp.objects.all()
    return render(request, "emp/home.html", {"emps": emps})
def add_employee(request):
    if request.method == "POST":
        # data Fetching from form
        emp_name = request.POST.get("emp_name")
        emp_id = request.POST.get("emp_id")
        emp_phone = request.POST.get("emp_phone")
        emp_email = request.POST.get("emp_email")
        emp_position = request.POST.get("emp_position")
        emp_address = request.POST.get("emp_address")
        emp_working = request.POST.get("emp_working")
        emp_department = request.POST.get("emp_department")
        # create an object for model to fetch data

        e = emp()
        e.name = emp_name
        e.emp_id = emp_id
        e.emp_phone = emp_phone
        e.email = emp_email 
        e.position = emp_position
        e.emp_address = emp_address
        e.emp_working = emp_working
        e.emp_department = emp_department
        if e.emp_working is None:
            e.emp_working = False
        else:
            e.emp_working = True
        e.save()  # Save the employee object to the database


        return redirect('/emp/home')  # Redirect to the same page after processing
    return render(request, "emp/add_employee.html")

def employee_edit(request, id):
    employee = get_object_or_404(emp, id=id)
    if request.method == "POST":
        # Update employee data from form
        employee.name = request.POST.get("emp_name")
        employee.emp_id = request.POST.get("emp_id")
        employee.emp_phone = request.POST.get("emp_phone")
        employee.email = request.POST.get("emp_email")
        employee.position = request.POST.get("emp_position")
        employee.emp_address = request.POST.get("emp_address")
        employee.emp_working = request.POST.get("emp_working") == 'on'
        employee.emp_department = request.POST.get("emp_department")
        try:
            employee.save()
            return redirect('/emp/home')
        except Exception as e:
            # Handle any validation errors
            return redirect('/emp/home')
    return redirect('/emp/home')

def employee_delete(request, id):
    employee = get_object_or_404(emp, id=id)
    employee.delete()
    return redirect('/emp/home')