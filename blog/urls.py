from django.urls import path
from .views import BlogListView, BlogDetailView


urlpatterns = [
    # I don't think exposing the primary key is safe...
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    path("", BlogListView.as_view(), name="home")
]
