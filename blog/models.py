from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=250)
    file = models.FileField(upload_to='posts/files/')
    description = models.TextField()
    image = models.ImageField(upload_to='posts/cover', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=True)

    def __str__(self):
        return str(self.title)