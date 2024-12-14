from . import views 
from django.urls import path 

urlpatterns = [ 
    path("lab8/task6", views.lab8_task6),
    path("students", views.show_students, name = 'show_students'),
    path('students/add', views.add_student),
    path('students/delete/<int:student_id>/', views.delete_student, name='delete_student'),
    path('teachers', views.show_teachers, name = 'show_teachers'),
    path('teacher/add', views.add_teacher)
]