from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView, CreateView,
    UpdateView, DeleteView
)

from .models import Employee
from .forms import EmployeeModelForm


class EmployeeListView(ListView):
    """ Employee list view """
    model = Employee
    template_name = 'list/employees.html'
    context_object_name = 'employees'


class EmployeeCreateView(CreateView):
    """ Employee create view """
    form_class = EmployeeModelForm
    model = Employee
    template_name = 'list/employees_add.html'
    success_url = '/'


class EmployeeUpdateView(UpdateView):
    """ Employee update view """
    form_class = EmployeeModelForm
    model = Employee
    template_name = 'list/employees_update.html'
    success_url = '/'


class EmployeeDeleteView(DeleteView):
    """ Employee delete view """
    model = Employee
    template_name = 'list/employees_delete.html'
    success_url = '/'
