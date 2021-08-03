from django.urls import path
from .views import (PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    UserPostListView)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name="blog-home"),
    path('user/<str:username>', UserPostListView.as_view(), name="user-posts"),
    # post/int:pk - pk is integer variable post primary key
    path('post/<int:pk>', PostDetailView.as_view(), name="post-detail"),
    # Both CreateView and UpdateView uses/share a url pattern model/_form
    path('post/new', PostCreateView.as_view(), name="post-create"),
    # post/<int:pk>/update/ - redirect a url based on the pk to update a post of a log in user
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post-update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post-delete"),
    path('about/', views.about, name='blog-about')
]

# When using PostListView class you use .as_view() to convert it as views
# But it has a specific html pattern to look at <app>/<model>_<viewtype>.html
# example: blog/post_list.html( blog - app, post - model, list - viewtype)