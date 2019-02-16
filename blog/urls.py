from django.contrib import admin
from django.urls import path, include
import blogapp.views
import portfolio.views
from django.conf import settings #암기 미디어파일 사용하기 위해서1
from django.conf.urls.static import static #암기 미디어파일 사용하기 위해서2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blogapp.views.home, name='home'),
    path('blog/',include('blogapp.urls')),
    path('portfolio/',portfolio.views.portfolio,name="portfolio"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
# + 이후에 있는거는 암기
#OR urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 로 써도됨
