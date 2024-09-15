from django.urls import path
from posts import views

urlpatterns = [
    path('', views.index, name='home'),
    path('posts/<slug:post_slug>/', views.categories),
]
