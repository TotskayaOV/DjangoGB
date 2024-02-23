from django.contrib import admin
from .models import Client, Product, Order
from django.utils.html import format_html


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'address', 'register_date']
    fieldsets = (('основные данные', {'fields': ['name']}),
                 ('контактные данные', {'fields': ['email', 'phone']}),
                 ('дополнительная информация', {'fields': ['address', 'register_date'], 'classes': ['collapse']}),)
    exclude = ['register_date']

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('register_date',)
        return self.readonly_fields


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'count', 'display_image']
    fieldsets = (
        ('основные данные продукта', {'fields': ['name']}),
        ('С1', {'fields': ['price', 'count']}),
        ('дополнительная информация', {'fields': ['description', 'image', 'register_date'], 'classes': ['collapse']}),
    )
    exclude = ['register_date']

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('register_date',)
        return self.readonly_fields

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.image.url))
        else:
            return format_html('<img src="/media/product_images/no_to_foto.png" width="50" height="50" />')

    display_image.short_description = 'Фото продукта'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['client_id', 'get_products_display', 'cost', 'register_date']
    fieldsets = (
        ('основные данные заказа', {'fields': ['client_id', 'cost', 'register_date']}),
        ('список продуктов', {'fields': ['get_products_display']}),
    )
    exclude = ['register_date']
    readonly_fields = ['get_products_display']

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ['register_date']
        return self.readonly_fields

    def get_products_display(self, obj):
        return ', '.join([str(product) for product in obj.product_id.all()])

    get_products_display.short_description = 'Продукты'
