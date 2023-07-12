from django.urls import path
from .views import BlogView, BlogDetail, BlogCreate, BlogEdit, BlogDelete

urlpatterns = [
    path('', BlogView.as_view(), name="home"),
    path('blog/create/', BlogCreate.as_view(), name="blog_create"),
    path('blog/<int:pk>/', BlogDetail.as_view(), name="blog_detail"),
    path('blog/<int:pk>/edit/', BlogEdit.as_view(), name="blog_edit"),
    path('blog/<int:pk>/delete/', BlogDelete.as_view(), name="blog_delete"),
]