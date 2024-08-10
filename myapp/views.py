from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.


def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        # print(user.is_superuser)
        if user is not None: 
            login(request, user)
            return redirect('/emp/home')
        else: 
            print(user) 
            return render(request, 'emp/signin.html',{'error': 'Invalid username or password' })

    return render(request, 'emp/signin.html')

def signup(request):
    if request.method=="POST":
        us=request.POST.get('username')
        ps1=request.POST.get('password1')
        ps2=request.POST.get('password2')
        if ps1!=ps2:
            return render(request,'emp/signup.html',{'username':us,'ps1':ps1,'ps2':ps2,'error':'Password must be same'})
        
        try : 
            User.objects.get(username=us)
            return render(request,'emp/signup.html',{'username':us,'error':'Username is not available'})
                
        except User.DoesNotExist:
            User.objects.create_user(username=us,password=ps1,is_active=True)
            return render(request, 'emp/signup.html', {'success': 'Account successfully created. Please sign in.'})
            
        except Exception as e:
            print('Unexpected error has occur : ',e)
    return render(request,'emp/signup.html')

def mylogout(request):  
    logout(request)
    return redirect('/signin')     

def protected_page(request):
    return render(request,'protected_page.html')
    
def index(request):
    return render(request,'index.html')

def about(request):
    print(request.path)
    return render(request,'about.html')