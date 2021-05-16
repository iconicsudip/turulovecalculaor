from django.shortcuts import render,redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from pcapp.models import Profile, submit
from django.contrib.auth.decorators import login_required
import string
import random
# Create your views here.
def main_view(request,link):
    #print(link)
    return render(request,'main.html',{'url':link})
def genpass():
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_characters) for i in range(10))
    return password
def genurl():
    return ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(7))
@login_required(login_url='/signin/')
def dashboard(request,uname=None):
    if not uname or uname is None:
        return redirect('signin')
    else:
        try:
            uid = User.objects.get(username = uname)
            #print(uid)
            if str(uid)==str(request.user):
                uid = User.objects.get(username = uname)
                #print(uid)
                url = Profile.objects.filter(user = uid).values_list('url',flat=True).first()
                password = Profile.objects.filter(user = uid).values_list('password',flat=True).first()
                usrnme= submit.objects.filter(user = uid).values_list('name',flat=True)
                lovername = submit.objects.filter(user = uid).values_list('lover_name',flat=True)
                #print(usrnme) 
                #print(lovername)
                extract_name = []
                for i in range(len(usrnme)):
                    extract_name.append([usrnme[i],lovername[i]])
                #print(extract_name)
                return render(request,'dashboard.html',{'url':url,'uname':uid,'pass':password,'extract_name':extract_name})
            else:
                auth.logout(request)
                return redirect('signin')
        except User.DoesNotExist:
            return redirect('signin')
def thankyou(request,url):
    usr = Profile.objects.get(url=url)
    return render(request,"thankyou.html",{'name':usr})
def submitted(request,url):
    #print(url)
    if(request.POST['name1'] and request.POST["name2"]):
        usr = Profile.objects.get(url=url)
        uid = User.objects.get(username=usr)
        #print(uid)
        #print(usr)
        #print(str(usr) == str(uid))
        if(str(usr) == str(uid)):
            #print(1)
            profile_submit = submit(user = uid,name = request.POST['name1'],lover_name = request.POST["name2"])
            profile_submit.save()
            return redirect('thankyou',url=url)
        else:
            messages.error(request,'Link Invalid')
            return redirect('main_view',link = url)
    else:
        return redirect('main_view',link = url) 
def signup(request):
    if not request.user.is_authenticated:
        if(request.method == 'POST'):
            if(request.POST["username"] and request.POST["email"]):
                u = User.objects.filter(username=request.POST["username"]).first()
                if(str(u) == request.POST["username"]):
                    #print(u)
                    messages.error(request,"Username Already Exists")
                    return redirect(signup)
                else:
                    try:
                        user = User.objects.get(email=request.POST["email"])
                        return render(request,"signin.html",{'error':request.POST["email"]+'already exists'})
                    except User.DoesNotExist:
                        user_password = genpass()
                        uemail = request.POST['email']
                        user = User.objects.create_user(username = request.POST["username"],email = request.POST["email"],password = user_password)
                        user.save()
                        checkuser = User.objects.get(email=uemail)
                        auth.login(request,checkuser)
                        name = User.objects.get(username=request.POST['username'])
                        #print(name)
                        gen = False
                        while not gen:
                            reff_url = genurl()
                            check = Profile.objects.filter(url=reff_url)
                            if not check:
                                #print(reff_url)
                                profile = Profile(user = name,password = user_password,url=reff_url)
                                profile.save()
                                messages.success(request,"Welcome to your dashboard.")
                                return redirect('dashboard',uname=name)
                            else:
                                continue
            else:
                return render(request,"signin.html",{'error':'Please fill all fields'})
        else:
            return render(request,'signin.html')
    else:
        messages.error(request,"You are already Logged In")
        return redirect('dashboard',uname=request.user)
def logout(request):
    auth.logout(request)
    messages.success(request,'You are now logged out.')
    return redirect('/')
def signin(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            if request.POST['email'] and request.POST['password']:
                useremail = User.objects.get(email=request.POST.get('email'))
                #print(useremail)
                password = request.POST.get('password')
                try:
                    user = auth.authenticate(request,username=useremail,password=password)
                    #print(user)
                    if user is not None:
                        auth.login(request, user)
                        messages.success(request, "You are successfully logged in now")
                        return redirect('dashboard',uname=user)
                    else:
                        messages.error(request, "Invalid Credentials,Please try again")
                        return redirect("signin")
                except User.DoesNotExist:
                    return render(request, 'signin.html', {'error': "User doesnot exists"})
            else:
                return render(request, 'signin.html', {'error': "Enter correct password or email address or username"})
        else:
            return render(request, 'signin.html')
    else:
        messages.error(request,"You are already Logged In")
        return redirect('dashboard',uname=request.user)