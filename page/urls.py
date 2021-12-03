from django.urls import path
from .views import list_article, get_article

urlpatterns = [
    path('', list_article, name="list_article"),
    path('category/<str:category>/', list_article, name="list_article_category"),
    path('article/<str:slug>', get_article, name="get_article"),
]
