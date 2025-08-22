from django.urls import path
from . import views

urlpatterns = [
    path("students/", views.studentsView),
    path("students/<str:id>/", views.studentDetailView),
    path("employees/", views.Employees.as_view()),
    path("employees/<str:id>/", views.EmployeeDetail.as_view()),
]
