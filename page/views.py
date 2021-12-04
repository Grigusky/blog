from django.shortcuts import render
from .models import UserDescription, BlogPost, BlogCategory, Comment


def list_article(request, category=None):
    """ list article with category """
    if category:
        return render(
            request, "article/list.html",
            {"articles": BlogPost.objects.filter(category=BlogCategory.objects.get(title=category))}
        )
    return render(request, "article/list.html", {"articles": BlogPost.objects.all()})


def get_article(request, slug=None):
    """ get an article with category"""
    article = BlogPost.objects.get(slug=slug)
    if request.POST:
        comment = request.POST.get("comment")
        user = request.user
        commentaire = Comment(article=article, content=comment, author=user)
        commentaire.save()
    return render(
        request, "article/get.html",
        {
            "article": article,
            "author_description": UserDescription.objects.get(user=article.author),
            "comments": Comment.objects.filter(article=article)
        }
    )
