from django.shortcuts import redirect, render
from studentapp.models import studentRegisterModel


# Create your main app views here.
def main_app(request):
    return render(request,"main/main-home.html")

def main_about(request):
    return render(request,"main/main-about.html")


def main_student_login(request):
    if request.method == "POST":
        email=request.POST.get("emaill")
        password=request.POST.get("passwordd")

        try:
            check=studentRegisterModel.objects.get(student_email=email,student_password=password)
            request.session['user_id']=check.user_id

            return redirect('student-home')

        except:
            pass
    return render(request,"main/main-student-login.html")

def main_student_register(request):
    if request.method=="POST":
        fullname=request.POST.get("fullname")
        studentID=request.POST.get("studentID")
        email=request.POST.get("email")
        password=request.POST.get("password")

        studentRegisterModel.objects.create(student_fullname=fullname,student_email=email,student_password=password,student_id=studentID)

    return render(request,"main/main-student-register.html")
def main_contact(request):
    return render(request,"main/main-contact.html")