from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.conf import settings
from users.models import Profile


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey('User', on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='post_pics', verbose_name=("Image"), null=True, blank=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):        
        return reverse('blog_detail', kwargs={'pk': self.pk})

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey('users.Profile', on_delete=models.CASCADE, related_name='author')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text


class User(Profile):
    pass