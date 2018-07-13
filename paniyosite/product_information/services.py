from .models import Product


def get_all_products():
    products = Product.objects.all()
    return products