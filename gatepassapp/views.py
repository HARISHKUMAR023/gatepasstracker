from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def logout_view(request):
    logout(request)
    return redirect('login_view')
# Create your views here.
def index(request):
    return render(request,'index.html')


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
            messages.success(request,'Login successful')
            request.session['user_type'] = user.user_type
            print(f"User type: {request.session['user_type']}")  # print user_type
            return redirect('dashboard')
        else:
            print(f"Failed login attempt with email: {email}")
            messages.error(request,'Invalid email and password')
     
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
    return render(request,'inc/applicationform.html',context)

@login_required
def approvals(request):
    user_type = request.session.get('user_type', 'default')
    context={
        'title':'approvels',
        'user_type': request.session.get('user_type', 'default'),
    }
    return render(request, 'pages/aprovels.html',context)