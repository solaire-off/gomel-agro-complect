from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .models import Item, Category, Detail
from orders.forms import OrderForm


def items_list(request):
    items = Item.objects.filter(published=True, category__published=True).order_by('-created_date')
    category = Category.objects.filter(published=True).order_by('title')
    order_form = OrderForm
    query = request.GET.get('q')
    query_category = request.GET.get('category')
    if query:
        items = Item.objects.filter(
            Q(published=True),
            Q(title__icontains=query) |
            Q(description__icontains=query)
            ).distinct().order_by('-created_date')
        if not query_category is None:
            query_category = get_object_or_404(Category, url=query_category)
            items = [ item for item in items if item.category.url==query_category.url ]
    paginator = Paginator(items,8)
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items  = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    context = {
        'query_category' : query_category,
        'form' : order_form,
        'query' : query,
        'items': items,
        'category': category
    }
    return render(request, 'catalog/catalog_items.html', context)

def items_by_category(request, category_url):
    selected_category = get_object_or_404(Category, url=category_url)
    items = Item.objects.filter(category=selected_category, published=True).order_by('-created_date')
    category = Category.objects.filter(published=True).order_by('title')
    context = {
        'category':category,
        'selected_category': selected_category,
        'items': items,
    }
    return render(request, 'catalog/catalog_items.html',context)


def single_item(request, category_url, item_url):
    item = get_object_or_404(Item,url=item_url)
    if not item.published or not item.category.published: raise Http404
    category = Category.objects.filter(published=True).order_by("title")
    details = Detail.objects.filter(items=item, published=True)
    order_form = OrderForm
    context = {
        'item':item,
        'category':category,
        'details':details,
        'form': order_form
    }
    return render(request,'catalog/single_item.html', context)

