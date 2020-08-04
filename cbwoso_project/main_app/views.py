from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import EmployeeForm
from .models import Employee, Position

# Create your views here.


def employerList(request):
    employers_list = Employee.objects.all()
    context = {'employers_list':employers_list}
    return render(request, 'main_app/employer_list.html', context)

def employerForm(request, id=0):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        if id == 0:
            # create a form instance and populate it with data from the request:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance=employee)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return redirect('employerlist')

    # if a GET (or any other method) we'll create a blank form
    else:
        if id==0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        context = {'form': form}
    return render(request, 'main_app/employer_form.html', context)

def employerDelete(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('employerlist')