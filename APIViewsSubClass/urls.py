
from django.contrib import admin
from django.urls import path
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', views.EmployeeListAPIView.as_view()),
    path('createapi/', views.EmployeeCreateAPIView.as_view()),
    path('retrieveapi/<int:pk>/', views.EmployeeRetrieveAPIView.as_view()),
    path('updateapi/<int:pk>/', views.EmployeeUpdateAPIView.as_view()),
    path('deleteapi/<int:pk>/', views.EmployeeDestroyAPIView.as_view()),
    path('listcreateapi/', views.EmployeeListCreateAPIView.as_view()),
    path('retrieveupdateapi/<int:pk>/', views.EmployeeRetrieveUpadteAPIView.as_view()),
    path('retrievedestroyapi/<int:pk>/', views.EmployeeRetrieveDestroyAPIView.as_view()),
    path('retrieveupdatedestroyapi/<int:pk>/', views.EmployeeRetrieveUpdateDestroyAPIView.as_view()),
]
