from django.shortcuts import render
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
