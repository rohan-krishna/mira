import sweetify

from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse

def user_login(request):
    
    if request.method == 'POST':
        # do something for the POST
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        next = request.POST['next']

        if user:
            if user.is_active:
                login(request, user)
                sweetify.success(request, 'Success!', text="You have been successfully logged in.", persistent="Yeah!")

                if next != "":
                    return redirect(next)
                else:
                    return redirect("tasks:index")

            else:
    
                return HttpResponse("Account Not Active")
        else:
            
            sweetify.error(request, 'Heads Up!.',text='Username and password mismatch. Try again please.', persistent="Ok")
            return redirect("household:user_login")
    else:

        return render(request, "household/login.html", {})
    
# Create your views here.
@login_required
def user_logout(request):
    
    logout(request)
    
    sweetify.info(request, 'Heads Up!', text="You have been logged out successfully.", persistent="Ok!")

    return redirect("tasks:index")
