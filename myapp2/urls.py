from django.urls import path
from . import views
from .views import ProductsHistoryView, ClientOrdersView, create_product, success_page, edit_product
from django.conf import settings
from django.conf.urls.static import static


urlpatterns =[
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('products_history/<int:client_id>/', ProductsHistoryView.as_view(), name='products_history'),
    path('client_orders/<int:client_id>/', ClientOrdersView.as_view(), name='client_orders'),
    path('create_product/', create_product, name='create_product'),
    path('success/', success_page, name='success_page'),
    path('edit_product/<int:product_id>/', edit_product, name='edit_product'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)