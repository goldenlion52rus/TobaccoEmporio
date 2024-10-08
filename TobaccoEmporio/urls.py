from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),
    path('posts/', include('posts.urls')),
    path('about/', include('about.urls')),
]
