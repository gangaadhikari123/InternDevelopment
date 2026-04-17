# from django.shortcuts import render
# from django.http import JsonResponse
# from students.models import Student
# from employees.models import Employee
# from .serializers import StudentSerializer, EmployeeSerializer
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.views import APIView


# # ---------------- STUDENT FUNCTION BASED VIEWS ----------------

# @api_view(['GET', 'POST'])
# def studentsview(request):
#     if request.method == 'GET':
#         students = Student.objects.all()
#         serializer = StudentSerializer(students, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def studentDetailview(request, pk):
#     try:
#         student = Student.objects.get(pk=pk)
#     except Student.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = StudentSerializer(student)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = StudentSerializer(student, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

#     elif request.method == 'DELETE':
#         student.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# # ---------------- EMPLOYEE CLASS BASED VIEWS ----------------

# class EmployeesView(APIView):

#     def get(self, request):
#         employees = Employee.objects.all()
#         serializer = EmployeeSerializer(employees, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors)


# class EmployeeDetailView(APIView):

#     def get_object(self, pk):
#         try:
#             return Employee.objects.get(pk=pk)
#         except Employee.DoesNotExist:
#             return None

#     def get(self, request, pk):
#         employee = self.get_object(pk)
#         if not employee:
#             return Response({"error": "Not found"}, status=404)

#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         employee = self.get_object(pk)
#         if not employee:
#             return Response({"error": "Not found"}, status=404)

#         serializer = EmployeeSerializer(employee, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

#     def delete(self, request, pk):
#         employee = self.get_object(pk)
#         if not employee:
#             return Response({"error": "Not found"}, status=404)

#         employee.delete()
#         return Response({"message": "Deleted successfully"})


#Adding clean code for  viewset 
from rest_framework import viewsets
from students.models import Student
from employees.models import Employee
from .serializers import StudentSerializer, EmployeeSerializer


# STUDENT VIEWSET
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# EMPLOYEE VIEWSET
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
