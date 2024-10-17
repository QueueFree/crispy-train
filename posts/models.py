from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Post(models.Model):
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=100, null=False, blank=False)
    content = models.TextField(null=True, blank=True)
    rate = models.IntegerField(max_length=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name='posts')

    def __str__(self):
        return f'Этот пост о: {self.title}'

    objects = models.Manager()


class Category(models.Model):
    text = models.CharField(max_length=49)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='category')


class Comment(models.Model):
    text = models.CharField(max_length=1000)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

