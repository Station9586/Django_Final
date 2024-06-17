from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Account, LoginForm
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

# def login(request):
#     request.session['is_login'] = False
#     # from Account to get the data and see whether account and psw is correct
#     is_login = -1
#     try: 
#         username = request.GET['login_username']
#         password = request.GET['login_password']
#     except:
#         # print(is_login)
#         # is_login = 0
#         message = "Please Fill in all the information"
#         return render(request, 'main/index.html', locals())
#     try:
#         account = Account.objects.get(username=username)
#         # print(account.password)
#         if account.password == password:
#             if (account.nickname == "Admin"):
#                 return redirect('/admin')
#             is_login = 1
#         else:
#             message = "Invalid account or password"
#             return render(request, 'main/index.html', locals())
#     except:
#         message = "Invalid account or password"
#         return render(request, 'main/index.html', locals())

#     if is_login == 1:
#         request.session['is_login'] = True
#         request.session['username'] = username
#         message = "Login successfully"
#     # print(is_login)
#     return redirect('/main/pg1')
#     # return render(request, 'member/main.html', locals())

def login (request): 
    request.session['is_login'] = False
    is_login = -1
    if (request.method == 'POST'): 
        login_form = LoginForm(request.POST)
        if (login_form.is_valid()):
            login_name = request.POST['username'].strip()
            login_password = request.POST['password']
            user = authenticate(username = login_name, password = login_password)
            if (user is not None): 
                if (user.is_active): 
                    auth.login(request, user)
                    message = "Login successfully"
                    request.session['is_login'] = True
                    request.session['username'] = login_name
                    return redirect('/admin')
                else: message = "帳號尚未啟用"
            else: 
                account = Account.objects.get(username=login_name)
                if account.password == login_password:
                    is_login = 1
                    request.session['is_login'] = True
                    request.session['username'] = login_name
                    message = "Login successfully"
                    return redirect('/main/pg1')
                else: message = 'Invalid account or password'
        else: message = 'Please Check the information'
    else: login_form = LoginForm()


    return render(request, 'main/index.html', locals())


def register (request): 
    is_register = -1;
    try: 
        username = request.GET['username']
        password = request.GET['password']
        confirm = request.GET['password_again']
        if password != confirm:
            message = "Password does not match"
            print("Not match")
            return render(request, 'main/new_member.html', locals())
        else:
            try: 
                find = Account.objects.get(username=username)
                if (find):
                    message = "Username already exists"
                    print("Username already exists")
                    return render(request, 'main/new_member.html', locals())
            except:
                is_register = 1
                account = Account.objects.create(username=username, password=password)
                account.save()
                # message = "Register successfully"
                # return render(request, 'main/new_member.html', locals())
    except:
        print("input are not complete")
        message = "input are not complete"
        return render(request, 'main/new_member.html', locals())
    if is_register == 1:
        message = "Register successfully"
        print("Register successfully")
    return render(request, 'main/index.html', locals())
