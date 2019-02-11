from django.shortcuts import render,get_object_or_404,redirect
from .models import Blog
from django.utils import timezone #timezone사용방법
def home(request):
    blogs = Blog.objects #쿼리셋
    return render(request,'home.html',{'blogs' : blogs})
def detail(request, blog_id):
   blog_detail = get_object_or_404(Blog,pk=blog_id)#이용자가 원하는 몇 번 블로그 객체
   return render(request,'detail.html',{'blog':blog_detail})
def new(request): #new.html 띄워주기
   return render(request, 'new.html')
# Create your views here.
def create(request):
   blog = Blog()
   blog.title = request.GET['title']
   blog.body = request.GET['body']
   blog.pub_date = timezone.datetime.now()
   blog.save()
   return redirect('/blog/'+str(blog.id))