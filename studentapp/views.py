from email import message
from django.shortcuts import render,redirect,get_object_or_404
from studentapp.models import *
from librarianapp.models import *
from django.db.models import Q
from django.contrib import messages
from adminapp.models import *
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from django.core.paginator import Paginator


# Create your student app views here.
def student_register(request):
    if request.method == "POST" and request.FILES["photo"]:
        fullname=request.POST.get("fullname")
        studentID=request.POST.get("studentID")
        branch=request.POST.get("branch")
        year=request.POST.get("year")
        email=request.POST.get("email")
        password=request.POST.get("password")
        photo=request.FILES["photo"]
        student_data = studentRegisterModel.objects.create(student_fullname=fullname,student_email=email,student_password=password,student_id=studentID,student_photo=photo,student_branch=branch,student_year=year)
        student_data.save()
        if student_data:
            messages.success(request,"successfully registered")
        else:
            messages.error(request,"Your form is not registered, please try again")
    return render(request,"main/main-student-register.html")

def student_login(request):
    if request.method == "POST":
        email=request.POST.get("emaill")
        password=request.POST.get("passwordd")
        print("sssss")

        try:
            # print("cccccc")
            check=studentRegisterModel.objects.get(student_email=email,student_password=password)
            request.session['user_id']=check.user_id
            print("lllll")
            if check.student_status == 'accepted':
                messages.success(request,'Successfully Login')
                return redirect('student-home')
            elif check.student_status == 'pending':
                messages.warning(request,'Your request is in pending, please wait for until acceptance')
            elif check.student_status == 'rejected':
                messages.error(request,'Your request is rejected, so you cannot login')
        except:
                messages.warning(request,'invalid login')
    return render(request,"main/main-student-login.html")

def student_home(request):

    user_id=request.session['user_id']
    data=AddingBooksModel.objects.count()
    issu=ViewBooks.objects.filter(stu_id__user_id__icontains=user_id,librarian_status="Issued").count()
    ret=ViewBooks.objects.filter(stu_id__user_id__icontains=user_id,return_book_status="Returned").count()
    # issu=ViewBooks.objects.filter(stu_id=user_id).filter(librarian_status="accepted").count()
    # print(issu)
    # ret=ViewBooks.objects.filter(stu_id=user_id).filter(return_book_status="completed").count()

    return render(request,"student/STD-home.html",{'data':data,'issu':issu,'ret':ret})

def student_search_book(request):
   fPosts = AddingBooksModel.objects.all()
   paginator = Paginator(fPosts, 4)
   page_number = request.GET.get('page')
   page_obj = paginator.get_page(page_number)

   if request.method == "POST":
        print("something")
        z=request.POST.get("title")
        search=request.POST.get("search")
        
        if z == "Book Title":
            fPosts = AddingBooksModel.objects.filter(Q(booktitle__icontains=search))
        elif z == "Author name":
            fPosts = AddingBooksModel.objects.filter(Q(authorname__icontains=search))
        elif z == "Department":
            fPosts = AddingBooksModel.objects.filter(Q(department__icontains=search))
        elif z == "Publisher":
            fPosts = AddingBooksModel.objects.filter(Q(publisher__icontains=search))
        elif z == "Edition":
            fPosts = AddingBooksModel.objects.filter(Q(edition__icontains=search))
        else:
            fPosts = AddingBooksModel.objects.all()

        
        print('xytgt4tgtgrgrg.......',z)
        print("fff")
        page_obj = AddingBooksModel.objects.filter(Q(booktitle__icontains=search) | Q(authorname__icontains=search) | Q(department__icontains=search) | Q(publisher__icontains=search) | Q(edition__icontains=search)).all()
        print("jjj",page_obj)
        return render(request,"student/STD-search-book.html",{'d1':page_obj})
   return render(request,"student/STD-search-book.html",{'d1':page_obj})

def student_mylibrary(request):
    id=request.session['user_id']
    my=ViewBooks.objects.filter(stu_id=id)

    return render(request,"student/STD-mylibrary.html",{'my':my})

def student_return_books(request,id,id2):
    
    decline = get_object_or_404(ViewBooks,stu_id=id,view_id=id2)
    decline.return_book_status = "Returned"
    decline.save(update_fields=["return_book_status"])
    accept = ViewBooks.objects.get(view_id=id2)

    return redirect('student-return-books')

def student_myprofile(request):
    user_id=request.session['user_id']
    c=studentRegisterModel.objects.filter(user_id=user_id)
    x = studentRegisterModel.objects.get(user_id=user_id)
    if request.method=="POST" :
        name=request.POST.get("fullname")
        branch=request.POST.get("branch")
        email=request.POST.get("email")
        password=request.POST.get("password")
       
    
        x.student_fullname=name
        x.student_branch=branch
        x.student_email=email
        x.student_password=password
        
        x.save(update_fields=['student_fullname','student_branch','student_email','student_password'])
        x.save()
    # if request.method=="POST":
    #     obj = get_object_or_404(studentRegisterModel,user_id=user_id)
    #     obj.student_fullname=request.POST.get("fullname")
    #     obj.student_branch=request.POST.get("branch")
    #     obj.student_email=request.POST.get("email")
    #     obj.student_password=request.POST.get("password")
    #     obj.save()
    return render(request,"student/STD-myprofile.html",{'d':c})

def student_update_profile(request,id):
    user_id=request.session['user_id']
    x = studentRegisterModel.objects.filter(student_id=id)
    if request.method=="POST" and request.FILES["photo"]:
        name=request.POST.get("name")
        branch=request.POST.get("branch")
        email=request.POST.get("email")
        password=request.POST.get("password")
        photo=request.FILES["photo"]
    
        x.student_fullname=name
        x.student_branch=branch
        x.student_email=email
        x.student_password=password
        x.student_photo=photo
        x.save(update_fields=['student_fullname','student_branch','student_email','student_password','student_photo'])
        x.save()
    
    return render(request,"student/student-update-profile.html",{'x':x})

def student_feedback(request):
    id=request.session['user_id']

    data=studentRegisterModel.objects.get(user_id=id)
    if request.method == "POST":
        rating3=request.POST.get("rating3")
        text=request.POST.get("text")
        
        # text analysis
        analysis = TextBlob(text,analyzer=NaiveBayesAnalyzer())
        print(analysis.sentiment)
        
        sentiment = ''
        if analysis.polarity >= 0.5:
            sentiment = 'Very Positive'
        elif analysis.polarity > 0 and analysis.polarity < 0.5:
            sentiment = 'Positive'
        elif analysis.polarity < 0 and analysis.polarity > -0.5:
            sentiment = 'Negitive'
        elif analysis.polarity <= -0.5:
            sentiment = 'Very Negitive'
        else:
            sentiment = 'Neutral'


        student_feedback = StudentFeedbackModel.objects.create(rating3=rating3,text=text,student_id=data,sentiment=sentiment)
        student_feedback.save()
        messages.success(request,"Successfully Sent")    
        
    return render(request,"student/STD-feedback.html")

# def student_view_book(request,id):
#     data=AddingBooksModel.objects.filter(book_id=id)
#     print(data)
#     return render(request,"student/STD-view-book.html",{'data':data})

# def student_purchase_request(request,id):
#     user_id1=request.session['user_id']
#     data=AddingBooksModel.objects.get(book_id=id)
#     data1=studentRegisterModel.objects.get(user_id=user_id1)
#     print(data,data1)
#     # obj=ViewBooks.objects.create(librarian_id=data,stu_id=data1)
#     # obj.save()
#     return redirect('student-search-book')
    
def student_view_book(request,id):
    user_id1=request.session['user_id']
    data=AddingBooksModel.objects.filter(book_id=id)
    obj=ViewBooks.objects.filter(stu_id=user_id1,librarian_id=id) 
    print(obj)
    
    print(data)
    return render(request,"student/STD-view-book.html",{'data':data,"obj":obj})

def student_purchase_request(request,id):
    user_id1=request.session['user_id']
    print(user_id1)
    data=AddingBooksModel.objects.get(book_id=id)
    data1=studentRegisterModel.objects.get(user_id=user_id1)
    print(data,data1)
    obj=ViewBooks.objects.create(librarian_id=data,stu_id=data1)
    obj.save()
    if obj:
        messages.success(request,'sucessfully Requested')
    return redirect('student-search-book')

def student_return(request,id):   
    user_id1=request.session['user_id']
    # data=AddingBooksModel.objects.get(book_id=id)
    # data1=studentRegisterModel.objects.get(user_id=user_id1)
    
    obj=ViewBooks.objects.filter(stu_id=user_id1,librarian_id=id)
    print(obj)
    obj2=get_object_or_404(ViewBooks,stu_id=user_id1,view_id=id)
    a=obj2.return_book_status = 'Processing'
    print(a)
    # student_id=user_id1
    # book_id=id
    # return_status="Processing"
    # data2=return_book.objects.create(stu_id=student_id,book_id=book_id,return_status=return_status)
   
    obj2.save(update_fields=['return_book_status'])
    if obj:
        messages.success(request,'Willing to return the book')
    return redirect('student-mylibrary')