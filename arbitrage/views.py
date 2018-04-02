from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views import View
# Websocket

from os import path
import sys, os
from .forms import UserRegistrationForm
# 包装csrf请求，避免django认为其实跨站攻击脚本
from django.views.decorators.csrf import csrf_exempt
from dwebsocket import accept_websocket,require_websocket
from .models import *
# 数据库
from .models import User
sys.path.append(os.path.join(os.path.dirname(__file__), '../../BitcoinMonitor/scripts/api').replace('\\', '/'))
from libs.api_manager import *
from libs.db_helper import *


# Create your views here.

class MainPage(View):
    def get(self, request):
        print(request.method)
        # return HttpResponse("Ture")
        return render(request, 'trade/index.html')

    def post(self, request):
        print(request.method)
        # return HttpResponse("False")
        return render(request, 'trade/index.html')


# 登录限制标识
@login_required
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


@csrf_exempt
def interface_test(request):
    if request.method == 'POST':
        # 最后返会给前端的数据，如果能在前端弹出框中显示我们就成功了
        #p = ApiManager()
        #a = p.query()

        account_balance(request)
        trade_history(request)

        # player = TestData(lastname="aaaaaa")
        # player.firstname = 'ttttt'
        # player.save()
        # d = TestData.objects.all()
        # print(d)
        a = "testing"
        return HttpResponse(a)
    else:
        return HttpResponse("<h1>test</h1>")


# 从api获取balance信息存入db
def account_balance(request):
    api_manager = ApiManager()
    ab = api_manager._get_account_balance()
    if ab is not None:
        db_helper._insert_account_balance(ab)
        pass
    pass


# 从api获取交易记录信息存入db
def trade_history(request):
    api_manager = ApiManager()
    th = api_manager._get_trade_history()
    if th is not None:
        db_helper._insert_trade_history(th)
        pass
    pass


def start_trade(request):
    pass


def stop_trade(request):
    pass


def transfer(request):
    pass


def order(request):
    pass

@accept_websocket
def echo(request):
    if not request.is_websocket():#判断是不是websocket连接
        try:#如果是普通的http方法
            message = request.GET['message']
            return HttpResponse(message)
        except:
            return render(request, 'index.html')
    else:
        request.websocket.send('ttttttttttttt'.encode(encoding="utf-8"))
        print ('is socket')
        for message in request.websocket:
            print(message)
            #if request.websocket is None:
            #    break
            request.websocket.send('ttttttttttttt'.encode(encoding="utf-8"))
        #request.websocket.send('ttttttttttttt'.encode(encoding="utf-8"))
        pass
        #for message in request.websocket:
        #   request.websocket.send(message)#发送消息到客户端
