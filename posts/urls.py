from django.urls import path
from posts import views


urlpatterns = [
    path('', views.index, name='home'),
    path('posts/<slug:post_slug>/', views.categories, name='categories'),
    path('posts/<int:post_id>/', views.show_post, name='posts'),
    path('addpage/', views.addpage, name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
]
