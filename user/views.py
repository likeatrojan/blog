from django.shortcuts import render,redirect  
from .forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            try: 
                User.objects.get(username=username)
                messages.add_message(request, messages.SUCCESS, 'Kullanıcı zaten kayıtlı.')
                return render(request,"register.html",{"form" : form})
            except User.DoesNotExist:
                newUser = User(username = username)
                newUser.set_password(password)
                newUser.save()
                login(request,newUser)
                messages.add_message(request, messages.SUCCESS, 'Başarıyla Kayıt Oldunuz.')
                return redirect("index")
        context = {
            "form" : form
        }
        return render(request,"register.html",context)


    else:
        form = RegisterForm()
        context = {
        "form":form
        }
        return render(request,"register.html",context)
    

def loginUser(request):
    form = LoginForm(request.POST or None)
    context = {
        "form" : form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username = username, password = password)
        if user is None:
            messages.add_message(request, messages.WARNING, 'Kullanıcı adı yada parola hatalı.')
        else:
            login(request, user)
            messages.add_message(request, messages.SUCCESS, 'Başarıyla giriş yaptınız.')
            return redirect("index")
    return render(request,"login.html", context)


def logoutUser(request):
    logout(request)
    messages.success(request,"Başarıyla Çıkış Yaptınız.")
    return redirect("index")

