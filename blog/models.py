from django.db import models
from django.contrib.auth.models import User

class PostModel(models.Model):
     title = models.CharField(max_length=100)
     content = models.TextField()
     author = models.ForeignKey(User, on_delete=models.CASCADE)
     date_created = models.DateTimeField(auto_now_add=True)
     likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)

     class Meta:
          ordering = ('-date_created',)

     def comment_count(self):
          return self.comment_set.all().count()

     def comments(self):
          return self.comment_set.all()
     
     def total_likes(self):
          return self.likes.count()
     
     def has_user_liked(self, user):
          return self.likes.filter(id=user.id).exists()

     def __str__(self):
          return self.title
     


class Comment(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
     content = models.CharField(max_length=200)
     date_added = models.DateTimeField(auto_now_add=True)

     def __str__(self):
          return self.content

     
