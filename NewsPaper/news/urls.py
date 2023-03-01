from django.urls import path

from .views import *


urlpatterns = [
   path('posts/', PostsList.as_view(), name='posts_list'),
   path('posts/<int:pk>/', PostDetail.as_view(), name='post_detail'),
   path('posts/search/', PostsSearch.as_view(), name='posts_search'),
   path('news/create/', NewsCreate.as_view(), name='news_create'),
   path('articles/create/', ArticlesCreate.as_view(), name='articles_create'),
   path('posts/<int:pk>/edit/', PostEdit.as_view(), name='post_edit'),
   path('posts/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   # path('posts/<int:pk>/edit/', ArticlesEdit.as_view(), name='articles_edit'),
   # path('posts/<int:pk>/delete/', ArticlesDelete.as_view(), name='articles_delete'),
]
