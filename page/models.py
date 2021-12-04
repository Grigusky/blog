from django.db import models
from django_quill.fields import QuillField
from django.conf import settings
from django.contrib.auth.models import User
from django_extensions.db.fields import AutoSlugField


class UserDescription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField()


class BlogCategory(models.Model):
    """ model for categories """

    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class BlogPost(models.Model):
    """ a model for a blog post """

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    category = models.ForeignKey(
        BlogCategory,
        on_delete=models.CASCADE,
        blank=True, null=True
    )
    date = models.DateField(auto_now=True)
    title = models.CharField(max_length=100)
    content = QuillField()
    slug = AutoSlugField(null=True, default=None, unique=True, populate_from='name')

    def __str__(self):
        return self.title


class Comment(models.Model):
    """ a model for a comment """

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    article = models.ForeignKey(
        BlogPost,
        on_delete=models.CASCADE,
    )
    date = models.DateField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return f"{self.author}: {self.date}"
