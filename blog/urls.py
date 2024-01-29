from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     path('home/', views.index, name='blog-index'),
     path('post_detail/<int:pk>/', views.post_detail, name='blog-post-detail'),
     path('post_edit/<int:pk>/', views.post_edit, name='blog-post-edit'),
     path('post_delete/<int:pk>/', views.post_delete, name='blog-post-delete'),
     path('post/<int:pk>/like/', views.LikeView, name='blog-like'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)