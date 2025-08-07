# mysite/urls.py Configuration
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')), # подключаем маршруты приложения pages
    path('news/', include('news.urls')),  # подключаем маршрут новостей
]