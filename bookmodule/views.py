from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Book
from django.db.models import Sum, Avg, Max, Min, Q
from .forms import BookForm
# Create your views here.



def index(request):
    return render(request, 'bookmodule/index.html')


def index2(request, val1 = 0): 
    return HttpResponse("value1 = "+str(val1))

def viewbook(request, bookId):
    book = get_object_or_404(Book, pk=bookId)
    return render(request, 'bookmodule/show.html',{'book': book} )

def search(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
    # now filter
        books = __getBooksList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower(): contained = True
            if not contained and isAuthor and string in item['author'].lower():contained = True
            if contained: newBooks.append(item)
        return render(request, 'bookmodule/bookList.html', {'books':newBooks})
    return render(request, 'bookmodule/search.html')

def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]

def simple_query(request):
    mybooks= Book.objects.filter(title__icontains='and') # <- multiple objects
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})

def lookup_query(request):
    mybooks=books=Book.objects.filter(author__isnull = False).filter(title__icontains='and').filter(edition__gte = 2).exclude(price__lte = 100)[:10]
    if len(mybooks)>=1:
        return render(request,'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')
    
def lab8_task1(request):
    mybooks = Book.objects.filter(price__lte=50)
    if len(mybooks)>=1:
        return render(request,'bookmodule/lab8_task1.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')
    
    
def lab8_task2(request):
    mybooks = Book.objects.filter(Q(edition__gt=2) & (Q(title__icontains='qu') | Q(author__icontains='qu'))) 
    if len(mybooks)>=1:
        return render(request,'bookmodule/lab8_task2.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')
    
def lab8_task3(request):
    mybooks = Book.objects.filter(Q(edition__lte=2) & ~Q(title__icontains='qu') & ~Q(author__icontains='qu'))
    if len(mybooks)>=1:
        return render(request,'bookmodule/lab8_task3.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')
    
    
def lab8_task4(request):
    mybooks = Book.objects.all().order_by('title')
    if len(mybooks)>=1:
        return render(request,'bookmodule/lab8_task4.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')
    
def lab8_task5(request):
    book_count = Book.objects.count()
    total_price = Book.objects.aggregate(total_price=Sum('price'))['total_price']
    average_price = Book.objects.aggregate(avg_price=Avg('price'))['avg_price']
    maximum_price = Book.objects.aggregate(max_price=Max('price'))['max_price']
    minimum_price = Book.objects.aggregate(min_price=Min('price'))['min_price']
    context = {
        'book_count': book_count,
        'total_price': total_price,
        'average_price': average_price,
        'maximum_price': maximum_price,
        'minimum_price': minimum_price,
    }

    return render(request, 'bookmodule/lab8_task5.html', context)
    
    
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            
            return redirect('viewbook',bookId = book.pk )  # Replace 'book_list' with the name of the view to redirect after saving
    else:
        form = BookForm()
    return render(request, 'bookmodule/add_book.html', {'form': form})


def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('viewbook', bookId =book.pk)  # Assuming you have a book detail view
    else:
        form = BookForm(instance=book)
    return render(request, 'bookmodule/edit_book.html', {'form': form, 'book': book})