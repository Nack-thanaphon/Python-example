from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import tb_news
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required


# Create your views here.
def handler404(request,exception):
    return render(request, 'pythonprojects/error404.html')

def index(request):
    content = tb_news.objects.all().order_by("-id")
    return render(request, 'pythonprojects/index.html', {'news': content})

@login_required(login_url="/login")
@permission_required('is_staff',login_url='/warnning')
def addnews(request):
    return render(request, 'pythonprojects/addnews.html')

# news_title	news_detail	news_photo	news_date


def addnewsdata(request):
    news_title = request.POST['news_title']
    news_detail = request.POST['news_detail']
    news_photo = request.FILES['news_photo']
    content = tb_news(news_title=news_title,
                      news_detail=news_detail, news_photo=news_photo)
    content.save()
    return redirect("/contentmanager")



@login_required(login_url="/login")
@permission_required('is_staff',login_url='/warnning')
def contentmanager(request):
    mydatanews = tb_news.objects.all()
    return render(request, 'pythonprojects/contentmanager.html', {'news': mydatanews})


def contentedit(request):
    id = request.GET['id']
    result = tb_news.objects.filter(pk=id)

    return render(request, 'pythonprojects/contentedit.html', {'result': result})


def contentupdate(request):
    id = request.POST['id']
    news_title = request.POST['news_title']
    news_detail = request.POST['news_detail']

    try:
        news_photo = request.FILES['news_photo']
    except KeyError:
        news_photo = None

    content = tb_news.objects.get(pk=id)
    content.news_title = news_title
    content.news_detail = news_detail

    if news_photo is not None:
        content.newphoto = news_photo
        content.save()
    return redirect("/contentmanager")


def contentdeleate(request):
    id = request.POST['id']
    content = tb_news.objects.get(pk=id)
    content.delete()
    return redirect("/contentmanager")


def contentresult(request):
    id = request.GET['id']
    content = tb_news.objects.filter(pk=id)
    return render(request, 'pythonprojects/result.html', {'result': content})


def register(request):
    return render(request, 'pythonprojects/register.html')


def registerdata(request):
    fname = request.POST['fname']
    em = request.POST['em']
    uname = request.POST['uname']
    fname = request.POST['fname']
    pword = request.POST['pword']
    repword = request.POST['repword']

    if pword == repword:
        if User.objects.filter(username=uname).exists():
            messages.error(request, "ชื่อผู้ใช้งานซ้ำในระบบ")
            return redirect("/register")

        elif User.objects.filter(email=em).exists():
            messages.error(request, "email ของคุณซ้ำในระบบ")
            return redirect("/register")
        else:
            user = User.objects.create_user(
                first_name=fname,
                email=em,
                username=uname,
                password=pword
            )
            user.save()
            return redirect("/login")


    else:
        messages.error(request, "password และ repassword ไม่ตรงกัน")
        return redirect("/register")


def login(request):
    if request.user.is_authenticated:
        return redirect("/index")
    return render(request, 'pythonprojects/login.html')


def logincheck(request):
    Username = request.POST['username']
    Password = request.POST['password']

    User = auth.authenticate(username=Username, password=Password)
    if User is not None:
        auth.login(request, User)
        return redirect("/index")
    else:
        messages.error(request, "ไม่พบผู้ใช้งานในระบบ")
        return redirect("/login")


def logoff(request):
    auth.logout(request)
    return redirect("/login")


def warnning(request):
    return render(request, 'pythonprojects/warnning.html')
