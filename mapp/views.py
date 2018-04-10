from django.shortcuts import render
from mapp.forms import UserProfileInfoForm, UserForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
# Create your views here.
def index(request):
    return render(request, 'mapp/index.html')


def reg(request):
    """

    :type request: object
    """
    registered = False

    if request.method == "POST":

        user_form = UserForm(request.POST)
        profile_form = UserProfileInfoForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm
        profile_form = UserProfileInfoForm
    return render(request, 'mapp/register.html', {'registered': registered,
                                                  'user_form': user_form,
                                                  'profile_form': profile_form})


def lgn(request):
    if request.method == 'POST':
        username = request.POST.get('Username')
        password =  request.POST.get('Password')
        user = authenticate(username= username, password= password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Not active')
        else:
            print('someone is failed')
            print('Username: {} and password'.format(username, password))
            return HttpResponse('invalid details')
    else:
        return render(request, 'mapp/login.html')
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))