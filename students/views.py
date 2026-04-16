from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def students(request):
    students=[
        {'id': 1, 'name': 'John Doe', 'age': 20},
        {'id': 2, 'name': 'Jane Smith', 'age': 22},
        {'id': 3, 'name': 'Sam Brown', 'age': 19}
    ]
    return HttpResponse('students')
