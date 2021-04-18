from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    belong = models.ForeignKey('boards.Board', on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(blank=True, null=True)
    view_count = models.PositiveSmallIntegerField(default = 0)
    class Meta:
        ordering = ('-published_date',) 

    def get_absolute_url(self):
        return reverse("boards:post_detail", kwargs={"pk": self.pk})
    
class Board(models.Model):
    board_name = models.CharField(max_length=50)
    about = models.CharField(max_length=50)
    established_date = models.DateTimeField(auto_now_add=True)
    visit_count = models.PositiveSmallIntegerField(default=0)
    class Meta:
        ordering = ('-established_date',) 

    def __str__(self):
        return self.board_name
    
class Favorite(models.Model):
    someone = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fav = models.CharField(max_length=10)
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)