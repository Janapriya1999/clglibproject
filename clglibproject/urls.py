"""clglibproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include 
from mainapp import views as mainapp_views
from adminapp import views as adminapp_views
from librarianapp import views as librarianapp_views
from studentapp import views as studentapp_views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    
    path('admin/', admin.site.urls),

    # main views
    path('', mainapp_views.main_app,name="main-home"),
    path('main-about',mainapp_views.main_about,name="main-about"),
    # path('main-admin-login',mainapp_views.main_admin_login,name="main-admin-login"),
    # path('main-librarian-login',mainapp_views.main_librarian_login,name="main-librarian-login"),
    path('main-contact',mainapp_views.main_contact,name="main-contact"),

    # admin views
    path('main-admin-login',adminapp_views.main_admin_login,name="main-admin-login"),

    path('adm-dashboard',adminapp_views.admin_dashboard,name="adm-dashboard"),
    path('adm-add-librarian',adminapp_views.admin_adm_add_librarian,name="adm-add-librarian"),
    path('adm-manage-librarian',adminapp_views.admin_adm_manage_librarian,name="adm-manage-librarian"),
    path('adm-view-std',adminapp_views.admin_adm_view_std,name="adm-view-std"),
    path('adm-manage-std',adminapp_views.admin_adm_manage_std,name="adm-manage-std"),
    path('accepted-student/<int:id>/',adminapp_views.accept_students,name="accepted-student"),
    path('declined-student/<int:id>/',adminapp_views.decline_students,name="declined-student"),
    path('adm-edit/<int:id>/',adminapp_views.admin_adm_edit,name="adm-edit"),
    path('adm-delete/<int:id>/',adminapp_views.admin_adm_delete,name="adm-delete"),
    path('adm-search-book',adminapp_views.admin_adm_search_book,name="adm-search-book"),
    path('adm-view-std-rece-book',adminapp_views.admin_adm_view_std_rece_book,name="adm-view-std-rece-book"),
    path('adm-view-return',adminapp_views.admin_adm_view_return,name="adm-view-return"),
    path('adm-view-all-book',adminapp_views.admin_adm_view_all_book,name="adm-view-all-book"),
    path('adm-manage-book',adminapp_views.admin_adm_manage_book,name="adm-manage-book"),
    path('adm-feedback',adminapp_views.admin_adm_feedback,name="adm-feedback"),
    path('adm-sentiment',adminapp_views.admin_sentiment,name="adm-sentiment"),



    # librarian views
    path('main-librarian-login',librarianapp_views.main_librarian_login,name="main-librarian-login"),

    path('lib-home',librarianapp_views.librarian_home,name="lib-home"),
    path('lib-add-book',librarianapp_views.librarian_add_book,name="lib-add-book"),
    path('lib-search',librarianapp_views.librarian_search,name="lib-search"),
    path('lib-profile',librarianapp_views.librarian_profile,name="lib-profile"),
    path('lib-view',librarianapp_views.librarian_view,name="lib-view"),
    # path('ib-search-book',librarianapp_views.librarian_search_book,name="ib-search-book"),
    path('accepted-book/<int:id>/',librarianapp_views.accept_book,name="accepted-book"),
    path('declined-book/<int:id>/',librarianapp_views.decline_book,name="declined-book"),
    path('accepted-return/<int:id>/',librarianapp_views.accept_return,name="accepted-return"),
    path('lib-issue-book',librarianapp_views.librarian_issue_book,name="lib-issue-book"),
    path('lib-return-book',librarianapp_views.librarian_return_book,name="lib-return-book"),
    path('lib-sentiment',librarianapp_views.librarian_sentiment,name="lib-sentiment"),
    # path('lib-sentiment-analysis',librarianapp_views.librarian_sentiment_analysis,name="lib-sentiment-analysis"),
    path('return_book_accept/<int:id>/<int:id2>/',librarianapp_views.return_book_accept,name="return_book_accept"),

    path('lib-view-bookdetails',librarianapp_views.librarian_view_bookdetails,name="lib-view-bookdetails"),
    path('lib-issued-book',librarianapp_views.librarian_issued_book,name="lib-issued-book"),
    path('lib-feedback',librarianapp_views.librarian_feedback,name="lib-feedback"),

    # student views
    path('main-student-register',studentapp_views.student_register,name="student-register"),
    path('main-student-login',studentapp_views.student_login,name="student-login"),

    path('student-home',studentapp_views.student_home,name="student-home"),
    path('student-search-book',studentapp_views.student_search_book,name="student-search-book"),
    path('student-mylibrary',studentapp_views.student_mylibrary,name="student-mylibrary"),
    path('student-myprofile',studentapp_views.student_myprofile,name="student-myprofile"),
    path('student-update-profile/<int:id>/',studentapp_views.student_update_profile,name="student-update-profile"),
    path('student-feedback',studentapp_views.student_feedback,name="student-feedback"),
    path('student-view-book/<int:id>/',studentapp_views.student_view_book,name="student-view-book"),
    path('student-return/<int:id>/',studentapp_views.student_return,name="student-return"),
    path('student-purchase-request/<int:id>/',studentapp_views.student_purchase_request,name="student_purchase_request"),
    path('student-return-books/<int:id>/',studentapp_views.student_return_books,name="student-return-books"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
