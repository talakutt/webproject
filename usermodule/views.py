from django.shortcuts import render,redirect,  get_object_or_404
from .models import Student, Address, Teacher
from django.db.models import Count
from .forms import StudentForm, TeacherForm

# city1 = Address.objects.create(city="New York")
# city2 = Address.objects.create(city="Los Angeles")
# city2.save()
# city1.save()
# std1 = Student.objects.create(name="John Doe", age=20, address=city1)
# std2 = Student.objects.create(name="Jane Smith", age=22, address=city2)
# std3 = Student.objects.create(name="Tom Har", age=22, address=city2)
# std1.save()
# std2.save()
# std3.save()


# Create your views here.
def lab8_task6(request):
    city_counts = Address.objects.values('city').annotate(student_count=Count('student')).order_by('-student_count')
    
    return render(request, 'usermodule/ctiyStudents.html', {'cities': city_counts})

def show_students(request): 
    studentList = Student.objects.all()
    return render(request, "usermodule/ShowStudents.html", {'students': studentList})


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            return redirect('show_students')
    else:
        form = StudentForm()
    return render(request, 'usermodule/add_student.html', {'form': form})

def delete_student(request, student_id):
    # Get the student object, or return a 404 if not found
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return redirect('show_students')

def add_teacher(request): 
    if request.method == 'POST':
        form = TeacherForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show_teachers')  # Change to the view you want to redirect to
    else:
        form = TeacherForm()
    return render(request, 'usermodule/add_teacher.html', {'form': form})


def show_teachers(request):
    teacherList = Teacher.objects.all()
    return render(request, 'usermodule/show_teachers.html', {'teachers': teacherList})