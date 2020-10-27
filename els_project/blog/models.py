from django.db import models
from django.utils.text import slugify

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="post_images")
    body = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True)

    def save(self):
        self.slug = slugify(self.title)
        super(Post, self).save()

    def __str__(self):
        return "%s" % self.title
