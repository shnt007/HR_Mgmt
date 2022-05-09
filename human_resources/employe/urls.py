from django.urls import path
from employe import views

urlpatterns = [
    path('emp', views.Emp, name="emp_detail"),
    path('show', views.show, name="emp_index"),
    path('edit/<int:id>', views.edit, name="emp_edit"),
    path('update/<int:id>', views.update, name="emp_update"),
    path('delete/<int:id>', views.delete, name="emp_delete")
]
