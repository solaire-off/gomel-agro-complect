from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .models import Service, Category
from orders.forms import OrderForm


def service_list(request):
    category = Category.objects.filter(published=True).order_by('title')
    query_category = request.GET.get('category')
    if query_category:
        service = Service.objects.filter(
            Q(published=True),
            Q(category__url=query_category)
            ).distinct().order_by('-created_date')
    paginator = Paginator(category,8)
    page = request.GET.get('page')
    try:
        category = paginator.page(page)
    except PageNotAnInteger:
        category  = paginator.page(1)
    except EmptyPage:
        category = paginator.page(paginator.num_pages)
    order_form = OrderForm
    context = {
        'query_category' : query_category,
        'category': category,
        'form' : order_form
    }
    return render(request, 'service/service_list.html', context)

def service_by_category(request, service_url):
    selected_category = get_object_or_404(Category, url=service_url)
    service = Service.objects.filter(category=selected_category, published=True).order_by('-created_date')
    category = Category.objects.filter(published=True).order_by('title')
    order_form = OrderForm
    context = {
        'category':category,
        'selected_category': selected_category,
        'service': service,
        'form' : order_form
    }
    return render(request, 'service/service_list.html',context)


def service_detail(request, category_url, service_url):
    service = get_object_or_404(Service,url=service_url)
    if not service.published or not service.category.published: raise Http404
    category = Category.objects.filter(published=True).order_by("title")
    order_form = OrderForm
    context = {
        'service': service,
        'category':category,
        'form' : order_form
    }
    return render(request,'service/service_detail.html', context)
