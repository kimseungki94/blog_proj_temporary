from django import forms
from .models import Blog

class BlogPost(forms.ModelForm):
   
#모델py에 블로그 객체를 받기위해서는 이렇게 forms.ModelForm 사용
    class Meta:
        model = Blog
        fields = ['title','body']


# forms.Form
#  email = forms.EmailField()
#     files = forms.FileField()
#     url = forms.URLField()
#     words = forms.CharField(max_length=200)
#     max_number = forms.ChoiceField(choices=[('1','one'),('2','two'),('3','three')])