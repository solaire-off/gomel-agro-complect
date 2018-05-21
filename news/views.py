from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import News, Tag
from django.db.models import Q

def news_list(request):
    news = News.objects.filter(published=True).order_by('-created_date')
    query = request.GET.get('q')
    if query:
        news = News.objects.filter(
            Q(published=True),
            Q(title__icontains=query) |
            Q(content__icontains=query)
            ).distinct().order_by('-created_date')
    context = {
            'news' : news,
            'query' : query
            }
    return render(request,'news/news.html', context)

def news_by_tag(request, tag_url):
    selected_tag = get_object_or_404(Tag, url=tag_url)
    news = News.objects.filter(tags__url__startswith=selected_tag.url, published=True).order_by('-created_date')
    context = {
            'news' : news,
            'selected_tag' : selected_tag
    }
    return render(request, 'news/news.html',context)
