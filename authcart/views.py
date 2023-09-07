from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# # Create your views here.
def signup(request):
    if(request.method=="POST"):
        email=request.POST['email']
        password=request.POST['pass1']
        confirm_password=request.POST['pass2']
        if password!=confirm_password:  
            messages.error(request,"Password is not matching")   
            return render(request,'signup.html')
        try:
            if User.objects.get(username=email):     
                #return HttpResponse("email is incorrect")    
                #return render(request,"auth/signup.html")
                messages.info(request,"Email is taken") 
                return render(request,'signup.html')  
        except Exception as identifier:
            pass
        user=User.objects.create_user(email,email,password)  
        user.save()
        messages.success(request,"User created successfully") 
        return redirect('/auth/signup')
        
    return render(request,"signup.html")


def handlelogin(request):

    if request.method=="POST":
        username=request.POST['email']
        userpassword=request.POST['pass1']
        myuser=authenticate(username=username,password=userpassword)
        if myuser is not None:
            login(request,myuser)
            messages.info(request,"login succesfully")   
            return redirect('/')
           
        else:
            messages.error(request,"Invalid credential")
            return redirect('/auth/login')
    return render(request,"login.html")



def handlelogout(request):
    logout(request)
    return redirect('/auth/login/')



