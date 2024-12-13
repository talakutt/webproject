from . import views 
from django.urls import path 


urlpatterns = [
    # path('', views.start)
    path('', views.index),
path('index2/<int:val1>/', views.index2),
path('<int:bookId>/', views.viewbook, name='viewbook'),
path('search/', views.search),
path('simple/query/', views.simple_query),
path('complex/query/', views.simple_query),
path("lab8/task1", views.lab8_task1),
path("lab8/task2", views.lab8_task2),
path("lab8/task3", views.lab8_task3),
path("lab8/task4", views.lab8_task4),
path("lab8/task5", views.lab8_task5),
path("add_book", views.add_book),
path('<int:pk>/update/', views.edit_book, name='update_book')
]