from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views import View
from os import path
import sys,os
from .forms import UserRegistrationForm
sys.path.append(os.path.join(os.path.dirname(__file__), '../../BitcoinMonitor/scripts/api').replace('\\', '/'))
from bithumb.easy_api import EasyAPI
from libs.api_manager import *
# Create your views here.


class Login(View):
    def get(self, request):
        print(request.method)
        return render(request, 'index.html')

    def post(self, request):
        print(request.method)
        return render(request, 'index.html')

class MainPage(View):
    def get(self, request):
        print(request.method)
        #return HttpResponse("Ture")
        return render(request, 'index.html')

    def post(self, request):
        print(request.method)
        #return HttpResponse("False")
        return render(request, 'index.html')

def index(request):
    # request.POST
    # request.GET
    bithumb_api=EasyAPI('','')
    res = bithumb_api.get_ticker('ALL')
    if res['status'] == '0000':
        print (res['data']['BTC']['buy_price'])
    test = ApiManager()
    testaaa = test.GetBithumbApi().get_account()
    print (testaaa)
    return HttpResponse("Ture")
    return render(request, "index.html",)

#@api_view(['POST', 'GET'])
def aaaa(request, *args):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass

def dashboard(request):
    return render(request,
                  'account/dashboard.html',
                  {'section': 'dashboard'})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'account/register.html',
                  {'user_form': user_form})

def login(request):
    return HttpResponse("Ture")