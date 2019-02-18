from django.shortcuts import render,get_object_or_404,redirect
from .models import Blog
from django.core.paginator import Paginator #페이지를 나눌때 사용하는 import
from django.utils import timezone #timezone사용방법
from .form import BlogPost
def home(request):
    blogs = Blog.objects #쿼리셋
    blog_list = Blog.objects.all() #블로그 모든 글들을 대상
    paginator= Paginator(blog_list, 3) #모든 블로그객체 3개씩 잘라주기!
    page = request.GET.get('page') #request 페이지가 뭔지를 알아내고 (request페이지를 변수에 담아낸다)
    posts=paginator.get_page(page)#request된 페이지를 얻어온뒤 return해준다
    return render(request,'home.html',{'blogs' : blogs, 'posts':posts})
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
def blogpost(request):
   #1. 입력된 내용을 처리하는 기능 -> Post
   if request.method == 'POST':
      form = BlogPost(request.POST)
      if form.is_valid():
         post = form.save(commit=False)
         post.pub_date = timezone.now()
         post.save()
         return redirect('home')
   #2. 빈페이지를 띄워주는 기능 ->GET
   else:
      form = BlogPost()
      return render(request,'new.html',{'form':form})







