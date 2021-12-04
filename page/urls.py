from django.conf.urls.static import static
from django.urls import path

from blog import settings
from .views import list_article, get_article

urlpatterns = [
    path('', list_article, name="list_article"),
    path('category/<str:category>/', list_article, name="list_article_category"),
    path('article/<str:slug>', get_article, name="get_article"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
