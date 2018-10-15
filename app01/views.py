from django.shortcuts import render ,redirect ,HttpResponse
from app01.models import *
# Create your views here.
def addbook(request):
    if request.method =="POST":
        title = request.POST.get("title")
        price= request.POST.get("price")
        pub_date = request.POST.get("pub_date")
        publish_id = request.POST.get("publish_id")
        authors_id_list= request.POST.getlist("authors_id_list")
        print (title,price,pub_date,publish_id ,authors_id_list)
        book_list = Book.objects.create(title=title,price=price,publishDate=pub_date,publish_id=publish_id)
        book_list.authors.add(*authors_id_list)
    publish_list = Publish.objects.all()
    authors_list = Author.objects.all()
    return render(request,"add.html" ,locals())
def book(request):
    book_lish = Book.objects.all()
    return render(request,"book.html",locals())
def chagebook(request,edit_book_id):
    book_list = Book.objects.filter(pk=edit_book_id).first()
    publish_list = Publish.objects.all()
    authors_list = Author.objects.all()
    if request.method == "POST":
        title = request.POST.get("title")
        price = request.POST.get("price")
        pub_date = request.POST.get("pub_date")
        publish_id = request.POST.get("publish_id")
        authors_id_list = request.POST.getlist("authors_id_list")
        Book.objects.filter(pk=edit_book_id).update(title=title,price=price,publishDate=pub_date,publish_id=publish_id)
        # book_list.authors.set(authors_id_list)
        book_list.authors.clear()
        book_list.authors.add(*authors_id_list)

        print (title,price,pub_date,authors_id_list)
        return redirect("/book/")
    return render(request ,"chagebook.html",locals())
def deletebook(request,edit_book_id):
    Book.objects.filter(pk=edit_book_id).delete()
    return redirect("/book")