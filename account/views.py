from django.shortcuts import render,redirect
from django.contrib.auth.models import User #유저클래스
from django.contrib import auth #계정권한
def signup(request):
    if request.method=='POST': #정보전달 방식으로 post로 지정했으므로
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user( username=request.POST['username'],password=request.POST['password1']) #계정생성
            auth.login(request,user) #자동로그인 목적
            return redirect('home') #바로이동! 
    return render(request,'signup.html')

def login(request):
    if request.method=='POST': #정보전달 방식으로 post로 지정했으므로
                username = request.POST['username']
                password = request.POST['password']
                user = auth.authenticate(request, username=username, password=password) #회원명단이 맞는지 확인!
                if user is not None:
                    auth.login(request,user)
                    return redirect('home')
                else:
                    return render(request, 'login.html', {'error': 'username or password is incorrect'})
    else:
        return render(request,'login.html')

def logout(request):
    if request.method== 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request,'login.html')