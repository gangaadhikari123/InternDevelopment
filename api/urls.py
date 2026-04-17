from django.urls import path
from . import views

urlpatterns = [
   path('students/', views.studentsview),
   path('students/<int:pk>/', views.studentDetailview),

   path('employees/', views.EmployeesView.as_view()),
   path('employees/<int:pk>/', views.EmployeeDetailView.as_view()),

]
