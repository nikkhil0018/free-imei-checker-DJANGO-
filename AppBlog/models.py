from django.db import models

from django.contrib.auth.models import User

class BlogModel(models.Model):
    blog_title = models.CharField(max_length=50)
    blog_content = models.TextField()
    blog_date = models.DateTimeField(auto_now_add=True)
    blog_author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Blog Model'

    def __str__(self):
        return self.blog_title