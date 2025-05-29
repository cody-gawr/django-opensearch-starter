from search.opensearch_client import client
from products.models import Product
from django.core.serializers.json import DjangoJSONEncoder
import json

INDEX_NAME = "products"

def index_product(product: Product):
    tag_names = list(product.tags.values_list('name', flat=True))

    doc = {
        "id": product.id,
        "name": product.name,
        "description": product.description,
        "tags": [pt.name for pt in product.tags.all()],
        "tag_vector": product.tag_vector or [],
    }

    client.index(
        index=INDEX_NAME,
        id=product.id,
        body=json.loads(json.dumps(doc, cls=DjangoJSONEncoder))
    )
