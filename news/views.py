from django.shortcuts import render
from .models import News

def news_list(request):
    news = News.objects.filter(published=True).order_by('-created_date')
    context = {
            'news' : news
            }
    return render(request,'news/news.html', context)
