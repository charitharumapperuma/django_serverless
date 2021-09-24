from django.urls import path

from api.views import EmployeeDetail, EmployeeList

urlpatterns = [
    path('api/employees/', EmployeeList.as_view()),
    path('api/employees/{id}', EmployeeDetail.as_view()),
]
