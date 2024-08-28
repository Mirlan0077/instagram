from django.urls import path
from . import views

app_name = 'api'


urlpatterns = [
    path('posts/', views.PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('likes/', views.LikeCreateView.as_view(), name='like-create'),
    path('likes/<int:pk>/', views.LikeDeleteView.as_view(), name='like-delete'),
]
