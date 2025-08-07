# news/views.py
from django.shortcuts import render
from .models import News_post

def news_list(request):
    """Отображает список всех новостей"""
    news_list = News_post.objects.all().order_by('-pub_date')  # новые сверху
    return render(request, 'news/news_list.html', {'news_list': news_list})