from django.db import models
from django.conf import settings
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    photo = models.ImageField(upload_to='images', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={"pk": self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE
    )

    def __str__(self):
        return self.comment

    def get_absolute_ulr(self):
        return reverse('post_list')