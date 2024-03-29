from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
# view function recieves a request and sends a response, reqeust handler.

from django.contrib import messages

from django.contrib import messages

from .decorator import unauthenticated_user, allowed_users
from .forms import CreateUserForm

from django.contrib.auth import authenticate, login, logout

from .models import userRole


def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            type = form.cleaned_data.get('type')
            messages.success(request, "Account was created for " + username)
            user = User.objects.get(username=username)
            user_data = userRole.objects.create(user=user, roleStatus=type)
            maint_group, created = Group.objects.get_or_create(name="Maintenance")
            users_group, created = Group.objects.get_or_create(name="users")
            if type == '0':
                user.groups.add(maint_group)
            elif type == '1':
                user.groups.add(users_group)
            user_data.save()
            return redirect('/login')
    context = {'form': form}
    return render(request, 'register.html', context)



def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(home)
        else:
            messages.info(request, "Username or Password is incorrect")

    context = {}
    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('/login')


@login_required(login_url='/login')
@allowed_users(allowed_roles=['users'])
def home(request):
    context = {}
    return redirect('/system')
    ##return render(request, "homepage.html", context)


