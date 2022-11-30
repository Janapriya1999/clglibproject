from django.db.models import Q
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from librarianapp.models import *
from studentapp.models import *
from adminapp.models import addingLibrarianModel
from django.core.paginator import Paginator

# Create your librarian app views here.
def main_librarian_login(request):
    
    if request.method == "POST":
        librarian_name=request.POST.get("username")
        print(librarian_name)
        librarian_password=request.POST.get("password")
        print(librarian_password)
        try:
            print("cccccc")
            check=addingLibrarianModel.objects.get(librarian_name=librarian_name,librarian_password=librarian_password)
            request.session['librarian_id']=check.librarian_id
            print("lllll")
            messages.success(request,'Successfully Login')
            return redirect('lib-home')
            # if check.student_status == 'accepted':
            # elif check.student_status == 'pending':
            #     messages.warning(request,'Your request is in pending, please wait for until acceptance')
            # elif check.student_status == 'rejected':
            #     messages.error(request,'Your request is rejected, so you cannot login')
        except:
            messages.warning(request,'invalid login')

    return render(request,"main/main-librarian-login.html")

def librarian_home(request):
    # data=AddingBooksModel.objects.values('authorname').count()
    user_id=request.session['librarian_id']
    profile=addingLibrarianModel.objects.filter(librarian_id=user_id)
    data=AddingBooksModel.objects.count()
    issu=ViewBooks.objects.all().count()
    studec=studentRegisterModel.objects.filter(student_status="declined").count()
    stureg=studentRegisterModel.objects.filter(student_status="accepted").count()
    bpen=ViewBooks.objects.filter(return_book_status="pending").count()
    bret=ViewBooks.objects.filter(return_book_status="Returned").count()
    # libr=addingLibrarianModel.objects.count()
    # studec=studentRegisterModel.objects.filter(student_status="declined").count()
    # data=AddingBooksModel.objects.count()
    # reg=studentRegisterModel.objects.count()
    # dec=studentRegisterModel.objects.filter(student_status="declined").count()
    # issu=ViewBooks.objects.filter(librarian_status="accepted").count()
    # pend=studentRegisterModel.objects.filter(student_status="pending").count()
    # ret=return_book.objects.filter(return_status="accepted").count()

    return render(request,"librarian/lib-home.html",{'data':data,'issu':issu,'studec':studec,'stureg':stureg,'bpen':bpen,'bret':bret,'profile':profile})

def librarian_sentiment(request):
    user_id=request.session['librarian_id']
    profile=addingLibrarianModel.objects.filter(librarian_id=user_id)
    fPosts=StudentFeedbackModel.objects.all()
    paginator = Paginator(fPosts, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    w = ViewBooks.objects.order_by('-view_id')
    
    return render(request,"librarian/lib-sentiment.html",{'r':w,'profile':profile,'data':page_obj})

def librarian_add_book(request):
    user_id=request.session['librarian_id']
    profile=addingLibrarianModel.objects.filter(librarian_id=user_id)
    if request.method == "POST" and request.FILES["photo"]:
        tit=request.POST.get("tit")
        auth=request.POST.get("auth")
        dep=request.POST.get("dep")
        pub=request.POST.get("pub")
        edi=request.POST.get("edi")
        Discription=request.POST.get("Discription")
        photo=request.FILES["photo"]

    
        adds=AddingBooksModel.objects.create(booktitle=tit,authorname=auth,department=dep,publisher=pub,edition=edi,bookphoto=photo,descripition=Discription,)
        request.session['book_id']=adds.book_id
        messages.success(request,"successfully Uploaded Book...")
        return redirect('lib-add-book')
        

    return render(request,"librarian/lib-add-book.html",{'profile':profile})
    
def librarian_search(request):
    user_id=request.session['librarian_id']
    profile=addingLibrarianModel.objects.filter(librarian_id=user_id)
    fPosts = AddingBooksModel.objects.all().order_by('-book_id')
    paginator = Paginator(fPosts, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if request.method == "POST":
        search=request.POST.get("search")

        d = AddingBooksModel.objects.filter(Q(booktitle__icontains=search))
    return render(request,"librarian/lib-searchhh.html",{'se':page_obj,'profile':profile})



# def librarian_search(request):
#    if request.method == "POST" and request.FILES["photo"]:
#         tit=request.POST.get("tit")
#         auth=request.POST.get("auth")
#         dep=request.POST.get("dep")
#         pub=request.POST.get("pub")
#         edi=request.POST.get("edi")
#         photo=request.FILES["photo"]
#         search=request.POST.get("search")

#         AddingBooksModel.objects.all(booktitle=tit,authorname=auth,department=dep,publisher=pub,edition=edi,bookphoto=photo)
#     return render(request,"librarian/lib-searchhh.html",{'d1': search})
# def librarian_search_book(request):
#     return render(request,"librarian/lib-search-book.html")
def librarian_issue_book(request):
    user_id=request.session['librarian_id']
    profile=addingLibrarianModel.objects.filter(librarian_id=user_id)
    
    

    fPosts = ViewBooks.objects.all().order_by('-view_id') 
    paginator = Paginator(fPosts, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # pagination_by=5
    
    # paginator=Paginator(librarian_issue_book, 3)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    return render(request,"librarian/lib-issue-book.html",{'r':page_obj,'profile':profile})
    # ,context={'pages':page_obj}
def accept_book(request,id):
    accept = get_object_or_404(ViewBooks,view_id=id)
    accept.librarian_status = "Issued"
    accept.save(update_fields=["librarian_status"])
    accept.save()

    return redirect("lib-issue-book")

def decline_book(request,id):
    decline = get_object_or_404(ViewBooks,view_id=id)
    decline.librarian_status = "Not Issued"
    decline.save(update_fields=["librarian_status"])
    decline.save()

    return redirect("lib-issue-book")

def accept_return(request,id):
    accept = get_object_or_404(ViewBooks,view_id=id)
    accept.return_book_status = "Returned"
    accept.save(update_fields=["return_book_status"])
    accept.save()

    return redirect("lib-issue-book")

def librarian_view_bookdetails(request):
    user_id=request.session['librarian_id']
    profile=addingLibrarianModel.objects.filter(librarian_id=user_id)
    return render(request,"librarian/lib-view-bookdetails.html",{'profile':profile})

def librarian_issued_book(request):
    user_id=request.session['librarian_id']
    profile=addingLibrarianModel.objects.filter(librarian_id=user_id)
    # issue=AddingBooksModel.objects.filter(book_id=id)
    # print(issue)
    return render(request,"librarian/lib-issued-book.html",{'profile':profile})

def librarian_feedback(request):
    user_id=request.session['librarian_id']
    profile=addingLibrarianModel.objects.filter(librarian_id=user_id)
    data=StudentFeedbackModel.objects.all()

    return render(request,"librarian/lib-feedback.html",{'data':data,'profile':profile})

def librarian_return_book(request):
    user_id=request.session['librarian_id']
    profile=addingLibrarianModel.objects.filter(librarian_id=user_id)
    fPosts=ViewBooks.objects.filter(librarian_status='issued').order_by('-view_id')
    paginator = Paginator(fPosts, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request,"librarian/lib-return-book.html",{'w':page_obj,'profile':profile})

def librarian_profile(request):
    user_id=request.session['librarian_id']
    c=addingLibrarianModel.objects.filter(librarian_id=user_id)
    profile=addingLibrarianModel.objects.filter(librarian_id=user_id)
    pp=addingLibrarianModel.objects.filter(librarian_id=user_id)
    if request.method=="POST":
        obj = get_object_or_404(addingLibrarianModel,librarian_id=user_id)
        # obj.student_fullname=request.POST.get("fullname")
        # obj.student_branch=request.POST.get("branch")
        # obj.student_email=request.POST.get("email")
        # obj.student_password=request.POST.get("password")
        obj.librarian_password=request.POST.get("password")
        obj.save()
        obj.save(update_fields=["librarian_password"])

    return render(request,"librarian/lib-profile.html",{'p':pp,'profile':profile,'c':c})

def librarian_view(request):
    user_id=request.session['librarian_id']
    profile=addingLibrarianModel.objects.filter(librarian_id=user_id)
    m=ViewBooks.objects.all()
    return render(request,"librarian/library-view.html",{'vv':m,'profile':profile})

# def issue_book(request,id):
#     issued = get_object_or_404(ViewBooks,view_id=id)
#     issued.librarian_status = "issued"
#     issued.save(update_fields=["book_status"])
#     issued.save()

#     return redirect("lib-view")

# def decline_book(request,id):
#     returned = get_object_or_404(ViewBooks,view_id=id)
#     returned.librarian_status = "returned"
#     returned.save(update_fields=["book_status"])
#     returned.save()

    # return redirect("lib-view")

def return_book_accept(request,id,id2):
    user_id=request.session['librarian_id']
    profile=addingLibrarianModel.objects.filter(librarian_id=user_id)
    # accept = ViewBooks.objects.get(view_id=id2)
    decline = get_object_or_404(ViewBooks,stu_id=id,view_id=id2)
    decline.return_book_status = "Returned"

    decline.save(update_fields=["return_book_status"])
    return redirect('lib-issue-book')
    

def accept_students(request,id):
    accept = get_object_or_404(studentRegisterModel,user_id=id)
    accept.student_status = "accepted"
    accept.save(update_fields=["student_status"])
    accept.save()

    return redirect('adm-manage-std')

def decline_students(request,id):
    decline = get_object_or_404(studentRegisterModel,user_id=id)
    decline.student_status = "declined"
    decline.save(update_fields=["student_status"])
    decline.save()

    return redirect('adm-manage-std')


    # return redirect("lib-issue-book")    