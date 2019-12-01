from django.shortcuts import render
from rest_framework.views import APIView
from testapp.serializers import EmployeeSerializer
from testapp.models import Employee
from rest_framework.response import Response
from rest_framework.generics import (
            ListAPIView,
            CreateAPIView,
            RetrieveAPIView,
            UpdateAPIView,
            DestroyAPIView,
            ListCreateAPIView,
            RetrieveUpdateAPIView,
            RetrieveDestroyAPIView,
            RetrieveUpdateDestroyAPIView,
        )

class EmployeeListAPIView(ListAPIView):
    # queryset = Employee.objects.all()  # default
    serializer_class = EmployeeSerializer

    # override this method to perform search operation
    # query_string: http://127.0.0.1:8000/api?ename=Sunny
    def get_queryset(self):
        qs = Employee.objects.all()
        name = self.request.GET.get('ename')
        if name is not None:
            qs = qs.filter(ename__icontains=name)
        return qs

class EmployeeCreateAPIView(CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeRetrieveAPIView(RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# for patch switch to raw input
class EmployeeUpdateAPIView(UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDestroyAPIView(DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeListCreateAPIView(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeRetrieveUpadteAPIView(RetrieveUpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


'''
So we can implement all the operation using just 2 endpoints -
By using class:
    1. ListCreateAPIView
    2. RetrieveUpdateDestroyAPIView

NOTE:- all the views are written, arrange urls properly
'''
