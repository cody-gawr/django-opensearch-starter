from celery import shared_task
from products.models import Product
from products.services.product_indexer import index_product

@shared_task
def index_product_task(product_id):
    try:
        product = Product.objects.select_related().prefetch_related('tags').get(id=product_id)
        index_product(product)
    except Product.DoesNotExist:
        pass