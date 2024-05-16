from django.shortcuts import render, redirect
from .models import Reservations, ReservationForm
from main.models import Account
import random

def random_id (): 
    ret = ""
    for i in range(0, 10):
        if (random.randint(0, 2) == 0): 
            ret += random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        else:
            ret += str(random.choice('0123456789'))
    return ret

# Create your views here.
def main (request):
    if (request.session.get('is_login') != True):
        return redirect('/')
    # print(f"name: {request.session.get('username')}")
    username = request.session.get('username')
    return render(request, 'member/main.html', locals())

def showdata (request): 
    if (request.session.get('is_login') != True):
        return redirect('/')
    username = request.session.get('username')
    # get all the reservations for the user
    is_delR = request.session.get('is_delR')
    message = request.session.get('message')
    request.session['is_delR'] = False
    request.session['message'] = None
    reservations = Reservations.objects.filter(Name__username=username)
    return render(request, 'member/showdata.html', locals())

def detete_r (request, id):
    if (request.session.get('is_login') != True):
        return redirect('/')
    # username = request.session.get('username')
    # get all the reservations for the user
    # reservations = Reservations.objects.filter(Name__username=username)
    # delete the reservation
    Reservations.objects.get(id=id).delete()
    request.session['is_delR'] = True
    request.session['message'] = "Reservation deleted successfully"
    return redirect('/main/pg2')

def go_reserve (request):
    if (request.session.get('is_login') != True):
        return redirect('/')
    
    username = request.session.get('username')
    is_reserve = request.session.get('is_reserve')
    request.session['is_reserve'] = False
    message = request.session.get('message')
    date = None; time = None; people = None; space = None
    try: 
        date = request.GET['date']
        time = request.GET['time']
        people = request.GET['people']
        space = request.GET['space']
        print(f"date: {date}, time: {time}, people: {people}, space: {space}")
        if (date == "" or time == "" or people == "" or space == ""):
            request.session['message'] = "Please fill in all the information_1"
            return redirect('/main/pg3')
            # return render(request, 'member/reserve.html', locals())

        elif (int(people) <= 0 or int(people) > 14):
            request.session['message'] = "Please enter a valid number of people"
            # return render(request, 'member/reserve.html', locals())
            return redirect('/main/pg3')
            # return render(request, 'member/reserve.html', locals())
        elif (Reservations.objects.filter(Date=date, Time=time, space=space).count() >= 1):
            request.session['message'] = "The space is already reserved"
            # return render(request, 'member/reserve.html', locals())
            return redirect('/main/pg3')
            # return render(request, 'member/reserve.html', locals())
        else: 
            print(f"username: {username}")
            try: 
                acc = Account.objects.get(username=username)
                Reservations.objects.create(Name=acc, Date=date, Time=time, people=people, space=space, id = random_id())
                request.session['is_reserve'] = True
                request.session['message'] = "Reservation successful"
            except:
                print(f"Error: username: {username}, date: {date}, time: {time}, people: {people}, space: {space}\n")
                request.session['message'] = "Reservation failed"
            return redirect('/main/pg3')

    except: 
        request.session['message'] = "Please fill in all the information_2"
    return render(request, 'member/reserve.html', locals())

def modify (request):
    if (request.session.get('is_login') != True):
        return redirect('/')
    username = request.session.get('username')
    reservations = Reservations.objects.filter(Name__username=username)
    is_modify = request.session.get('is_modify')
    message = request.session.get('message')
    request.session['is_modify'] = False
    request.session['message'] = None

    try:
        date = request.GET['date']
        time = request.GET['time']
        people = request.GET['people']
        space = request.GET['space']
        id = request.GET['old_id']
        if (date == "" or time == "" or people == "" or space == ""):
            request.session['message'] = "Please fill in all the information"
            return redirect('/main/pg4')
        elif (int(people) <= 0 or int(people) > 14):
            request.session['message'] = "Please enter a valid number of people"
            return redirect('/main/pg4')
        elif (Reservations.objects.filter(Date=date, Time=time, space=space).count() >= 1):
            request.session['message'] = "The space is already reserved"
            return redirect('/main/pg4')
        else: 
            Reservations.objects.filter(id=id).update(Date=date, Time=time, people=people, space=space)
            request.session['is_modify'] = True
            request.session['message'] = "Reservation modified successfully"
            return redirect('/main/pg4')
    except:
        request.session['message'] = "Please fill in all the information"

    return render(request, 'member/modify.html', locals())

def settings (request):
    if (request.session.get('is_login') != True):
        return redirect('/')
    
    is_modify = False
    message = request.session.get('msg')
    request.session['msg'] = None
    try: 
        username = request.session.get('username')
        old_psw = request.GET['old_psw']
        psw = request.GET['nw_password']
        confirm = request.GET['cf_password']
        if (old_psw == "" or psw == "" or confirm == ""):
            message = "Please Fill in the form"
            return render(request, 'member/settings.html', locals())
        if (psw != confirm):
            message = "Password does not match"
            return render(request, 'member/settings.html', locals())
        else:
            now_password = Account.objects.get(username=username).password
            if (now_password == psw):
                message = "Password is the same as the current one"
            elif (now_password != old_psw):
                message = "Old password is incorrect"
            else:
                is_modify = True
                Account.objects.filter(username=username).update(password=psw)
                message = "Password changed successfully"
    except:
        if (message == None):
            message = "Please Fill in the form"

    return render(request, 'member/settings.html', locals())

def change (request):
    if (request.session.get('is_login') != True):
        return redirect('/')
    request.session['is_modify'] = False
    try: 
        username = request.session.get('username')
        old_psw = request.GET['old_psw']
        psw = request.GET['nw_password']
        confirm = request.GET['cf_password']
        if (old_psw == "" or psw == "" or confirm == ""):
            request.session['message'] = "Please Fill in the form"
            return render(request, 'member/settings.html', locals())
        if (psw != confirm):
            request.session['message'] = "Password does not match"
            return render(request, 'member/settings.html', locals())
        else:
            now_password = Account.objects.get(username=username).password
            if (now_password == psw):
                request.session['message'] = "Password is the same as the current one"
            elif (now_password != old_psw):
                request.session['message'] = "Old password is incorrect"
            else:
                request.session['is_modify'] = True
                Account.objects.filter(username=username).update(password=psw)
                request.session['message'] = "Password changed successfully"
    except:
        request.session['message'] = "Please Fill in the form"
    return render(request, 'member/settings.html', locals())


def delete (request, old_psw):
    if (request.session.get('is_login') != True):
        return redirect('/')
    username = request.session.get('username')
    try: 
        if (old_psw == ""):
            request.session['msg'] = "Please Fill in the form"
            return redirect('/main/pg5');
        else:
            now_password = Account.objects.get(username=username).password
            if (now_password != old_psw):
                request.session['msg'] = "Old password is incorrect"
            else:
                acc = Account.objects.get(username=username)
                acc.delete()
                request.session.flush()
                return redirect('/')
    except:
        request.session['msg'] = "Please Fill in the Old Password"
    return redirect('/main/pg5');

def go_reserve2 (request):
    if (request.session.get('is_login') != True):
        return redirect('/')
    username = request.session.get('username')
    is_reserve = request.session.get('is_reserve')
    # print(f"is_reserve: {is_reserve}")
    request.session['is_reserve'] = False
    message = request.session.get('message')
    # print(f"message: {message}")
    if (request.method == 'POST'): 
        post_form = ReservationForm(request.POST)
        if (post_form.is_valid()):
            # check whether the space is already reserved
            date = post_form.cleaned_data['Date']
            time = post_form.cleaned_data['Time']
            space = post_form.cleaned_data['space']
            people = post_form.cleaned_data['people']
            if (Reservations.objects.filter(Date=date, Time=time, space=space).count() >= 1):
                request.session['message'] = "The space is already reserved"
                return redirect('/main/pg3')
            request.session['is_reserve'] = True
            request.session['message'] = "Reservation successful"
            post_form.save()
            return redirect('/main/pg3')
            # return render(request, 'member/reserve.html', locals())

        else:
            request.session['message'] = "Reservation failed"
            return redirect('/main/pg3')

    else:
        initial_data = {'Name': username, 'id': random_id()}
        post_form = ReservationForm(initial=initial_data)
        request.session['message'] = "Please fill in all the information"
        # return redirect('/main/pg3')
    return render(request, 'member/reserve.html', locals())