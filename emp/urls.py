from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('home/', employee_home, name='employee_home'),
    path('add/', add_employee, name='add_employee'),
    path('edit/<int:id>/', employee_edit, name='emp_edit'),
    path('delete/<int:id>/', employee_delete, name='emp_delete'),
]
