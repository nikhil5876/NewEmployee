from django.urls import path
from .views import emp_list, emp_form, emp_delete

urlpatterns = [
    path('',emp_list),
    path('add/',emp_form,name="insert_employee"),
    path('edit/<int:id>',emp_form,name="employee_update"),
    path('delete/<int:id>',emp_delete,name = "employee_delete"),
]
