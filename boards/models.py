from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length = 10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return f"{self.id}: {self.title}"
    

class Comment(models.Model):
    #on_delete는 필수 인자, on_delete는 참조하는 부모객체가 사라졌을때, 부모에 딸려있는 자식 객체들을 어떻게 처리할지 정의한다.
    # 부모객체의 소문자로 쓰는 것이 관례이다.
    board = models.ForeignKey(Board, on_delete = models.CASCADE)
    content = models.CharField(max_length = 200)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.content