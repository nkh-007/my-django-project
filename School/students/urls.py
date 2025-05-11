from django.urls import path
from .views import edit_student,delete_student,add_student,student_list,Mark_sheet_register,home,student_report,about_us,contact_us,user_login,logout_view
urlpatterns=[

path('', home,name='home'),
path('add/', add_student, name='add_student'),
path('list/', student_list, name='student_list'),
path('edit/<int:rollNumber>/',edit_student,name='edit_student'),
path('delete/<int:roll_number>/',delete_student,name='delete_student'),
path('register/', Mark_sheet_register, name='Mark_sheet_register'),
path('report/<int:roll_number>/', student_report, name='student_report'),
path('about/', about_us, name='about_us'),
path('contact/', contact_us, name='contact_us'),
path('login/', user_login, name='user_login'),
path('logout/', logout_view, name='logout_view'),


]

