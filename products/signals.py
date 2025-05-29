from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from products.models import ProductTag
from products.services.product_indexer import index_product

@receiver(m2m_changed, sender=ProductTag)
def reindex_product_on_tag_change(sender, instance, action, **kwargs):
    if action in ["post_add", "post_remove", "post_clear"]:
        index_product(instance)