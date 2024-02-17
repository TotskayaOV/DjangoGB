import logging
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views.generic import TemplateView
from datetime import datetime, timedelta
from .models import Order, Product, Client
from .forms import ProductForm


logger = logging.getLogger(__name__)


def logger_deco(funk):
    def wrapper(*args, **kwargs):
        request = args[0]
        logger.info(f"Посещена страница: {request.path}")
        return funk(*args, **kwargs)
    return wrapper


@logger_deco
def home(request):
    home_html = """
    <h1>Добро пожаловать на мой 2 сайт!</h1>
    <p>Здесь вы не найдете никакого контента.</p>
    """
    return render(request, 'home.html', {'content': home_html})


@logger_deco
def about(request):
    about_html = """
    <h1>Обо мне</h1>
    <p>здесь много информации обо мне 2</p>
    """
    return render(request, 'about.html', {'content': about_html})


class ClientOrdersView(TemplateView):
    template_name = 'orders_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client_id = self.kwargs.get('client_id')
        client = Client.objects.get(pk=client_id)
        orders = Order.objects.filter(client_id=client_id)
        context['client'] = client
        context['orders'] = orders
        return context


class ProductsHistoryView(TemplateView):
    template_name = 'products_history.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client_id = self.kwargs.get('client_id')
        orders_7_days = Order.objects.filter(client_id=client_id,
                                             register_date__gte=datetime.today() - timedelta(days=7)).distinct()
        orders_30_days = Order.objects.filter(client_id=client_id,
                                              register_date__gte=datetime.today() - timedelta(days=30)).distinct()
        orders_365_days = Order.objects.filter(client_id=client_id,
                                               register_date__gte=datetime.today() - timedelta(days=365)).distinct()
        products_7_days = Product.objects.filter(order__in=orders_7_days).distinct()
        products_30_days = Product.objects.filter(order__in=orders_30_days).distinct()
        products_365_days = Product.objects.filter(order__in=orders_365_days).distinct()
        context['client'] = Client.objects.get(pk=client_id)
        context['products_7_days'] = products_7_days
        context['products_30_days'] = products_30_days
        context['products_365_days'] = products_365_days
        return context


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('success_page'))
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form})


def success_page(request):
    return render(request, 'success_page.html')


def edit_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Перенаправление на страницу успеха

    return render(request, 'edit_product.html', {'form': form})
