from django.contrib import admin
from posts.models import Post
#from .models import Post # 이렇게 .models로 해도 됨. 같은 위치니까.

# Register your models here.
admin.site.register(Post) # 관리자도구를 이용하기 위해 필요함.