from django.urls import path 
from . import views


urlpatterns=[
    path('',views.login_view, name='login_view'),
    path('login/',views.login_view, name='login_view'),  
    path('logout/',views.logout_view, name='logout_view'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('chat/',views.chat, name = 'chat'),
    path('applicationform/',views.applicationfrom, name='applicationform'),
    path('approvals/',views.approvals, name='approvals'),
    path('requestform/',views.requestform, name='requestform'),
    path('staff/',views.staff, name='staff'),
    path('hod/',views.hod, name='hod'),
    path('warden/',views.warden, name='warden'),
    path('approve_studentstaff/<int:student_id>/',views.approve_studentstaff, name='approve_studentstaff'),
    path('approve_studenthod/<int:student_id>/',views.approve_studenthod, name='approve_studenthod'),
    path('rejection/<int:student_id>/',views.rejection, name='rejection'),
]