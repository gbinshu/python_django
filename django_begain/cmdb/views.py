from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
from cmdb import models

user_list = [
    {"user":"jack","pwd":"jack"},
    {"user":"tom","pwd":"tom"},
]

def index(request):
    if request.method=='POST':
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        print(username, password)
        #添加数据到数据库
        models.UserInfo.objects.create(user=username, pwd=password)
    # return HttpResponse("hello world!")

    # temp = {"user":username, "pwd":password}
    # user_list.append(temp)
    #从数据库中读取所有数据
    user_list = models.UserInfo.objects.all()
    '''
     当需要返回一个html文件时，需要用render来渲染
     第二个参数，指定页面
     第三个参数，是后台返回给浏览器的数据，它是一个字典，data是自定义的指针名字，会被对应的html文件引用
    '''
    return render(request, "index.html", {"data":user_list})