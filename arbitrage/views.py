from django.contrib.auth.decorators import login_required
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
        return render(request, 'trade/index.html')

    def post(self, request):
        print(request.method)
        return render(request, 'trade/index.html')

class MainPage(View):
    def get(self, request):
        print(request.method)
        #return HttpResponse("Ture")
        return render(request, 'trade/index.html')

    def post(self, request):
        print(request.method)
        #return HttpResponse("False")
        return render(request, 'trade/index.html')

@login_required #登录限制标识
def dashboard(request):
    return render(request,
                  'account/dashboard.html',
                  {'section': 'dashboard'})

@login_required
def mainpage(request):
    return render(request,
                  'trade/arbitrage_trade.html',
                  )

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

def comments_upload(request):
    print("fff")
    if request.method == 'POST':


        return HttpResponse("表单测试成功")  # 最后返会给前端的数据，如果能在前端弹出框中显示我们就成功了
    else:
        return HttpResponse("<h1>test</h1>")