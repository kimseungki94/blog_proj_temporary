from django.contrib import admin
from .models import Blog
from .models import Social

admin.site.register(Blog)
admin.site.register(Social)