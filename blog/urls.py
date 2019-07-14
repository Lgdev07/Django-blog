from django.urls import path
from . import views
from .views import PostListView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, LikedPostListView

urlpatterns = [
    path('', PostListView.as_view(), name='blog_home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user_posts'),
    path('liked/<str:username>', LikedPostListView.as_view(), name='liked_posts'),
    path('post/<int:pk>/', views.detail, name='blog_detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='blog_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='blog_delete'),
    path('post/new/', PostCreateView.as_view(), name='blog_create'),
    path('about/', views.about, name='blog_about'),
    path('contact/', views.contact, name='blog_contact'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    path('post/<int:pk>/like/', views.like_post, name='like_post'),
]

# pk = primary key