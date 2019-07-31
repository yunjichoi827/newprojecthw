from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog 
from django.utils import timezone


def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs' : blogs})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)

    return render(request, 'detail.html', {'blog':blog_detail})

def new(request):
    return render(request, 'new.html')

def create(request): #입력받은 내용을 데이터베이스에 넣어주는 함수
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))  #정보가 다 처리된 후에 url 로 넘기세요, 프로젝트 이외의 url 가능

def about(request):
    return render(request, 'about.html')