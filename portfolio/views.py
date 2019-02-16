from django.shortcuts import render
from .models import Portfolio
# Create your views here.
def portfolio(request): #new.html 띄워주기
   portfolios = Portfolio.objects
   return render(request, 'portfolio.html',{'portfolios':portfolios})