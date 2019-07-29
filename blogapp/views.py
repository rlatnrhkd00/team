

from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, Blogdealer, Blogquestion
from django.core.paginator import Paginator
from django.utils import timezone
from django.contrib.auth.models import User

# Create your views here.
def home (request):
    return render(request, 'home.html')


def freeboard (request):
    
    blogs = Blog.objects
    #블로그의 모든 글들을 대상으로
    blog_list = Blog.objects.all()
    #블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(blog_list,5)
    #request된 페이지가 뭔지를 알아내고 (request페이즈를 변수에 담아내고)
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 해준다
    posts = paginator.get_page(page)
    return render(request, 'freeboard.html', {'blogs':blogs, 'posts':posts})

def dealerboard (request):
    
    blogs = Blogdealer.objects
    #블로그의 모든 글들을 대상으로
    blog_list = Blogdealer.objects.all()
    #블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(blog_list,5)
    #request된 페이지가 뭔지를 알아내고 (request페이즈를 변수에 담아내고)
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 해준다
    posts = paginator.get_page(page)
    return render(request, 'dealerboard.html', {'blogs':blogs, 'posts':posts})

def questionboard (request):
    
    blogs = Blogquestion.objects
    #블로그의 모든 글들을 대상으로
    blog_list = Blogquestion.objects.all()
    #블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(blog_list,5)
    #request된 페이지가 뭔지를 알아내고 (request페이즈를 변수에 담아내고)
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 해준다
    posts = paginator.get_page(page)
    return render(request, 'questionboard.html', {'blogs':blogs, 'posts':posts})

def detail1 (request, blog_id):
    details = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'details':details})

def detail2 (request, blog_id):
    details = get_object_or_404(Blogdealer, pk = blog_id)
    return render(request, 'detail.html', {'details':details})

def detail3 (request, blog_id):
    details = get_object_or_404(Blogquestion, pk = blog_id)
    return render(request, 'detail.html', {'details':details})

def freeboardNew(request):
   # if User.is_authenticated:
   #    return render(request, 'login.html')
    #return render(request, 'login.html')
  #  else:
        return render(request, 'freeboardNew.html')

def dealerboardNew(request):
   # if User.is_authenticated:
   #    return render(request, 'login.html')
    #return render(request, 'login.html')
  #  else:
        return render(request, 'dealerboardNew.html')

def questionNew(request):
   # if User.is_authenticated:
   #    return render(request, 'login.html')
    #return render(request, 'login.html')
  #  else:
        return render(request, 'questionNew.html')
    


def blogCreate(request):
        blog1 = Blog()
        blog1.title = request.GET['title']
        blog1.body = request.GET['body']
        blog1.pub_date = timezone.datetime.now()
        blog1.save()
        
        return redirect('/blog/'+str(blog1.id))

def dealerCreate(request):
        blog2 = Blogdealer()
        blog2.title = request.GET['title']
        blog2.body = request.GET['body']
        blog2.pub_date = timezone.datetime.now()
        blog2.save()
        return redirect('/dealerboard/'+str(blog2.id))

def questionCreate(request):
        blog3 = Blogquestion()
        blog3.title = request.GET['title']
        blog3.body = request.GET['body']
        blog3.pub_date = timezone.datetime.now()
        blog3.save()
        return redirect('/questionboard/'+str(blog3.id))