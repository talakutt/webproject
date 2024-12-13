from django.shortcuts import render
from .models import Student, Address
from django.db.models import Count


city1 = Address.objects.create(city="New York")
city2 = Address.objects.create(city="Los Angeles")
city2.save()
city1.save()
std1 = Student.objects.create(name="John Doe", age=20, address=city1)
std2 = Student.objects.create(name="Jane Smith", age=22, address=city2)
std3 = Student.objects.create(name="Tom Har", age=22, address=city2)
std1.save()
std2.save()
std3.save()


# Create your views here.
def lab8_task6(request):
    city_counts = Address.objects.values('city').annotate(student_count=Count('student')).order_by('-student_count')
    
    return render(request, 'usermodule/ctiyStudents.html', {'cities': city_counts})


