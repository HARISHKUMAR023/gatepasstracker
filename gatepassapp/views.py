from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages



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
            login(request,user)
            messages.success(request,'Login successfull')
            return redirect('dashboard')
        else:
            print(f"Failed login attempt with email: {email}")
            messages.error(request,'Invaid email and password ')
     
    return render(request,'auth/login.html')

def dashboard(request):
    context = {
        'title': 'Dashboard',
    }
    return render(request,'dashboard/dashboard.html',context)