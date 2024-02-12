from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Student
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from twilio.rest import Client


def send_sms(request, student_id):
    student = get_object_or_404(Student, pk=student_id)

    # Your Twilio credentials
    account_sid = 'AC50662f4f946b263d3e60d3e911ea91c2'
    auth_token = '9e54110861e00e35a4d4be228fb1506d'
    twilio_phone_number = '+14325353444'

    # Initialize Twilio client
    client = Client(account_sid, auth_token)

    # Compose the SMS message
    message_body = f"Dear Parent, {student.Name} has been approved by the warden on today. Thank you!"

    # Send the SMS
    message = client.messages.create(
        to='+916369145671',  # Replace with the parent's phone number
        from_=twilio_phone_number,
        body=message_body
    )

    return HttpResponse(f"SMS sent! SID: {message.sid}")




def logout_view(request):
    logout(request)
    return redirect('login_view')
# Create your views here.
def index(request):
    return render(request,'index.html')


def requestform(request):
    try:
        if request.method == "POST":
            name = request.POST.get('name')
            rollnumber = request.POST.get('rollnumber')
            email = request.POST.get('email')
            department = request.POST.get('department')
            information = request.POST.get('information')
            student = Student.objects.create(Name=name , Rollnumber = rollnumber , Department = department , Infromation = information)
           
    except :
        messages.error(request,'Application form not submitted')
    return redirect('dashboard')
    
    return render(request,'dashboard/applicationform.html')

# def login(request):
#     context = {
#         'title': 'login',
#     }
#     return render(request,'auth/login.html',context)

def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request,username=email,password=password)
        if user is not None:
            print(f"User {user.username} authenticated")  # print username of authenticated user
            login(request,user)
           
            request.session['user_type'] = user.user_type
            print(f"User type: {request.session['user_type']}")  # print user_type
            return redirect('dashboard')
        else:
            print(f"Failed login attempt with email: {email}")
            
     
    return render(request,'auth/login.html')

@login_required
def dashboard(request):
 
    context = {
        'title': 'Dashboard',
        'user_type': request.session.get('user_type', 'default'),
    }
    return render(request,'dashboard/dashboard.html',context)

@login_required
def applicationfrom(request):
   
    context = {
        'title': 'Application Form',
        'user_type': request.session.get('user_type', 'default'),
        
    }
   
    return render(request,'pages/visual/applicationform.html',context)

def chat(request):
    context ={
        'title':'chat',
        'user_type': request.session.get('user_type', 'default'),
    
    }
    return render(request,'pages/visual/visulation.html',context)

@login_required
def approvals(request):
   
    context={
        'title':'approvels',
        'user_type': request.session.get('user_type', 'default'),
    }
    return render(request, 'pages/aprovels.html',context)


def staff(request):
    Students = Student.objects.filter(staff_approval=False , hod_approval=False, warden_approval=False, rejected=False)
    context ={
        'title':'staff',
        'user_type': request.session.get('user_type', 'default'),
        'students': Students
    }
    return render(request , 'pages/staffpages/staff.html', context )


def hod(request):
    Students = Student.objects.filter(staff_approval=True , hod_approval=False, warden_approval=False,rejected=False)
    
    context ={
        'title':'hod',
        'user_type': request.session.get('user_type', 'default'),
        'students':Students 
    }
    return render(request , 'pages/staffpages/hod.html', context )

def warden(request):
    Students = Student.objects.filter(staff_approval=True , hod_approval=True, warden_approval=False,rejected=False)
    context ={
        'title':'warden',
        'user_type': request.session.get('user_type', 'default'),
        'students':Students 
    }
    return render(request , 'pages/staffpages/warden.html', context )


def rejection(request, student_id):
   
    try:
        student = Student.objects.get(pk=student_id)
    except Student.DoesNotExist:
        # Handle the case where the student with the given ID doesn't exist
     
        return redirect('staff')  # or another view

    # Assuming there's a field in your Student model for rejection status (e.g., rejected)
    student.rejected = True
    student.save()
   
    return redirect('staff')  # or another view

def approve_studentstaff(request, student_id):
    try:
        student = Student.objects.get(pk=student_id)
    except Student.DoesNotExist:
        # Handle the case where the student with the given ID doesn't exist
       
        return redirect('staff')  # or another view

    # Assuming there's a field in your Student model for approval status (e.g., approved)
    student.staff_approval= True
    student.save()
 
    return redirect('staff') 

def approve_studenthod(request, student_id):
    try:
        student = Student.objects.get(pk=student_id)
    except Student.DoesNotExist:
        # Handle the case where the student with the given ID doesn't exist
     
        return redirect('hod')  # or another view

    # Assuming there's a field in your Student model for approval status (e.g., approved)
    student.hod_approval= True
    student.save()
   
    return redirect('hod') 


def approve_studentwarden(request, student_id):
    try:
        student = Student.objects.get(pk=student_id)
    except Student.DoesNotExist:
        # Handle the case where the student with the given ID doesn't exist
        messages.error(request, 'Student not found')
        return redirect('warden')  # or another view

    # Assuming there's a field in your Student model for warden approval status
    student.warden_approval = True
    student.save()

    # Assuming `send_sms` is a function that sends an SMS to the student's parent
    send_sms(request, student_id)

    messages.success(request, 'Student approved successfully')
    return redirect('warden')