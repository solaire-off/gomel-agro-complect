from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Item, Category, Detail

def items_list(request):
    items = Item.objects.filter(published=True)
    category = Category.objects.filter(published=True)
    context = {
        'items':items,
        'category':category
    }
    return render(request, 'catalog/catalog.html', context)

def details_list(request):
    list_detail = Detail.objects.filter(published=True)
    context = {
		'items' : list_detail
	}
    return render(request, 'catalog/catalog.html', context)

def items_by_category(request, category_url):
    selected_category = get_object_or_404(Category, url=category_url)
    items = Item.objects.filter(category=selected_category)
    category = Category.objects.filter(published=True)
    context = {
		'category':category,
		'selected_category': selected_category,
		'items': items,
	}
    return render(request, 'catalog/catalog.html',context)
