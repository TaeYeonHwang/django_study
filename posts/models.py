from django.db import models

# Create your models here.

class Post(models.Model):
  # 글의 제목, 내용, 작성일, 마지막 수정일.
  title = models.CharField(max_length=50)
  content = models.TextField() # max_length 지정 필요 X.
  dt_created = models.DateTimeField(verbose_name="Date Created.",auto_now_add=True) # auto_now_true : 처음 생성될 때 시간을 자동 저장. 값을 넣어주지 않아도 됨.
  dt_modified = models.DateTimeField(verbose_name="Date Modified.",auto_now=True)   # auto_now : 마지막으로 저장될 때 시간을 자동 저장. 값을 넣어주지 않아도 됨.
  
  def __str__(self):
    return self.title