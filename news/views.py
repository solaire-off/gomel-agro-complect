from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import News, Tag

def news_list(request):
    news = News.objects.filter(published=True).order_by('-created_date')
    context = {
            'news' : news
            }
    return render(request,'news/news.html', context)

def news_by_tag(request, tag_url):
    selected_tag = get_object_or_404(Tag, url=tag_url)
    news = News.objects.filter(tags__url__startswith=selected_tag.url, published=True).order_by('-created_date')
    context = {
            'news': news,
            'selected_tag' : selected_tag
    }
    return render(request, 'news/news.html',context)
