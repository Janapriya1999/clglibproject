from webbrowser import get
from django.shortcuts import render,redirect,get_object_or_404
from adminapp.models import *
from librarianapp.models import *
from studentapp.models import *
from django.contrib import messages
from clglibproject.settings import DEFAULT_FROM_EMAIL
from django.core.mail import EmailMultiAlternatives
from django.core.paginator import Paginator


# Create your admin app views here.
def main_admin_login(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        if username == "admin" and password == "admin":
            messages.success(request,'Successfully Login')
            return redirect('adm-dashboard')
        else:
            messages.warning(request,'invalid login')
            return redirect("main-admin-login")

    return render(request,"main/main-admin-login.html")

def admin_sentiment(request):
    user_id=request.session['librarian_id']
    profile=addingLibrarianModel.objects.filter(librarian_id=user_id)
    fPosts=StudentFeedbackModel.objects.all()
    paginator = Paginator(fPosts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    w = ViewBooks.objects.order_by('-view_id')

    return render(request,"admin/adm-sentiment.html",{'r':w,'profile':profile,'data':page_obj})

def admin_dashboard(request):
    # librarian_id=request.session['librarian_id']
    # profile=addingLibrarianModel.objects.filter(librarian_id=librarian_id)
    data=AddingBooksModel.objects.count()
    stureg=studentRegisterModel.objects.filter(student_status="accepted").count()
    libr=addingLibrarianModel.objects.count()
    studec=studentRegisterModel.objects.filter(student_status="declined").count()
    # issu=ViewBooks.objects.filter(stu_id=user_id).filter(librarian_status="accepted").count()
    # print(issu)
    # ret=ViewBooks.objects.filter(stu_id=user_id).filter(return_book_status="completed").count()

    # aa=AddingBooksModel.objects.count()
    # lib=addingLibrarianModel.objects.count()
    # stureg=studentRegisterModel.objects.count()
    # dec=studentRegisterModel.objects.filter(student_status="declined").count()
    # reg=studentRegisterModel.objects.count()


    return render(request,"admin/adm-dashboard.html",{'data':data,'stureg':stureg,'libr':libr,'studec':studec})

def admin_adm_add_librarian(request):
    if request.method=="POST" and request.FILES["photo"]:
        librarian_name=request.POST.get("name")
        librarian_phonenumber=request.POST.get("phonenumber")
        librarian_campusname=request.POST.get("campusname")
        librarian_blockname=request.POST.get("blockname")
        librarian_email=request.POST.get("email")
        librarian_password=request.POST.get("password")
        librarian_photo=request.FILES["photo"]

        
        adding=addingLibrarianModel.objects.create(librarian_name=librarian_name,librarian_phonenumber=librarian_phonenumber,librarian_campusname=librarian_campusname,librarian_blockname=librarian_blockname,librarian_email=librarian_email,librarian_password=librarian_password,librarian_photo=librarian_photo)
        request.session['librarian_id']=adding.librarian_id
        messages.success(request,'Successfully Added')
        html_content = "<strong> This Message Sent From college library management authority, Your resume has been selected for the <b> librarian position in engineering college </b> and your credentials are follow below: " + "<br>" + "username: " + str(librarian_name) + "<br>" + "email: " + str(librarian_email) + "<br>" + "password:" + str(librarian_password) + "<br>" + "Thank You For Your Registration. <strong>"
        from_mail = DEFAULT_FROM_EMAIL
        to_mail = [adding.librarian_email]
        # if send_mail(subject,message,from_mail,to_mail):
        msg = EmailMultiAlternatives("Account Registered Status", html_content, from_mail, to_mail)
        msg.attach_alternative(html_content, "text/html")
        if msg.send():
            print("Sent")
        
        return redirect('adm-add-librarian')
        
    return render(request,"admin/adm-add-librarian.html")

def admin_adm_manage_librarian(request):
    fPosts=addingLibrarianModel.objects.all().order_by('-librarian_id')
    paginator = Paginator(fPosts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # for i in admin_manage:
    #     print(i.librarian_photo)

    return render(request,"admin/adm-manage-librarian.html",{'data':page_obj})

def admin_adm_manage_std(request):
    fPosts=studentRegisterModel.objects.order_by("-user_id")
    paginator = Paginator(fPosts, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    for i in fPosts:
        print(i)
    
    return render(request,"admin/adm-manage-std.html",{'s':page_obj})
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

def admin_adm_view_std(request):
    fPosts=studentRegisterModel.objects.filter(student_status="accepted").order_by('-user_id')
    paginator = Paginator(fPosts, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request,"admin/adm-view-std.html",{'register':page_obj})

def admin_adm_delete(request,id):
    data=addingLibrarianModel.objects.filter(librarian_id=id).delete()
    # messages.success(request,"Successfully Delete Librarian Account")

    return redirect('adm-manage-librarian')

def admin_adm_edit(request,id):
    user_id=request.session['user_id']
    data = addingLibrarianModel.objects.filter(librarian_id=id)
    x = get_object_or_404(addingLibrarianModel,librarian_id=id)
    if request.method=="POST":
        name=request.POST.get("name")
        phonenumber=request.POST.get("phonenumber")
        campusname=request.POST.get("campusname")
        blockname=request.POST.get("blockname")
        email=request.POST.get("email")
        password=request.POST.get("password")
        # photo=request.FILES["photo"]
    
        x.librarian_name=name
        x.librarian_phonenumber=phonenumber
        x.librarian_campusname=campusname
        x.librarian_blockname=blockname
        x.librarian_email=email
        x.librarian_password=password
        x.save(update_fields=['librarian_name','librarian_phonenumber','librarian_campusname','librarian_blockname','librarian_email','librarian_password'])
        x.save()
    
    return render(request,"admin/adm-edit.html",{'x':data})

def admin_adm_search_book(request):
    return render(request,"admin/adm-search-book.html")

def admin_adm_view_std_rece_book(request):
    return render(request,"admin/adm-view-std-rece-book.html")

def admin_adm_view_return(request):
    return render(request,"admin/adm-view-return.html")

def admin_adm_view_all_book(request):
    return render(request,"admin/adm-view-all-book.html")

def admin_adm_manage_book(request):

    return render(request,"admin/adm-manage-book.html")

def admin_adm_feedback(request):
    data=StudentFeedbackModel.objects.all()

    return render(request,"admin/adm-feedback.html",{'data':data})
