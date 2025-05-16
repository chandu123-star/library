from django.shortcuts import render , redirect
from .models import Book
# Create your views here.
def create(request):
    var = True
    if request.method == "POST":
        book_name = request.POST.get('Bname')
        author = request.POST.get('author')
        isbn = request.POST.get('num')
        genere = request.POST.get('genere')
        prize = request.POST.get('prize')
        # print(book_name,author,isbn,genere,prize)
        Book.objects.create(name = book_name,author = author,isbn_number = isbn,genre = genere , prize = prize)
        print("successfully added")
        return redirect("display")
    context = {
        'var':var
    }

    return render(request,'create.html',context)


def display(request):
    data = Book.objects.all()
    context = {
        'daata':data
    }
    return render(request,'display.html',context)
 
def single(request,vk):
    # pk = 1
    single_data = Book.objects.get(id = vk)
    print(single_data)
    context = {
        'data':single_data
    }
    return render(request,'single.html',context)

def update(request,id):
    var = False
    data = Book.objects.get(id = id)
    if request.method == "POST":
        book_name = request.POST.get('Bname')
        author = request.POST.get('author')
        isbn = request.POST.get('num')
        genere = request.POST.get('genere')
        prize = request.POST.get('prize')
        # print(book_name,author,isbn,genere,prize)
        data.name  , data.author , data.isbn_number , data.genre , data.prize= book_name , author , isbn , genere , prize
        data.save()
        return redirect("display")

    context = {
        'data':data, 
        'var':var
    }
    return render(request,'edit.html',context)


def delete(request , pk):
    data = Book.objects.get(id = pk)
    data.delete()
    return redirect("display")