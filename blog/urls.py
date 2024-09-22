from django.urls import path

from blog.apps import BlogConfig
from blog.views import (BlogPostDeleteView,
                        BlogPostCreateView,
                        BlogPostListView,
                        BlogPostDetailView,
                        BlogPostUpdateView)

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogPostListView.as_view(), name='blogpost_list'),
    path('view/<int:pk>', BlogPostDetailView.as_view(), name='blogpost_detail'),
    path('create/', BlogPostCreateView.as_view(), name='blogpost_create'),
    path('edit/<int:pk>', BlogPostUpdateView.as_view(), name='blogpost_update'),
    path('delete/<int:pk>/', BlogPostDeleteView.as_view(), name='blogpost_confirm_delete')
]