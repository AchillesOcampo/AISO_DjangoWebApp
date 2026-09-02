from django.urls import path
from . import views

urlpatterns = [
    path("", views.student_list, name="student_list"),
    path("add/", views.create_student, name="student_create"),
    path("edit/<int:id>/", views.update_student, name="student_update"),
    path("delete/<int:id>/", views.delete_student, name="student_delete"),
    path("dashboard/", views.student_dashboard, name="student_dashboard"),
]