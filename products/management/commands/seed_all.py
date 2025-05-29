from django.core.management.base import BaseCommand
from products.factories import ProductFactory, TagFactory, ProductTagFactory
from products.models import Tag, Product, ProductTag
from products.services.product_indexer import index_product
import random

class Command(BaseCommand):
    help = "Seed products, tags, and product-tags with factory_boy"

    def add_arguments(self, parser):
        parser.add_argument('--products', type=int, default=10)
        parser.add_argument('--tags', type=int, default=5)
        parser.add_argument('--taggings', type=int, default=30)

    def handle(self, *args, **options):
        # Clean up old data
        self.stdout.write("🧹 Clearing existing product data...")
        ProductTag.objects.all().delete()
        Product.objects.all().delete()
        Tag.objects.all().delete()

        self.stdout.write("🌱 Creating new seed data...")

        tags = TagFactory.create_batch(options['tags'])
        products = ProductFactory.create_batch(options['products'])

        # Link products and tags via ProductTag
        for _ in range(options['taggings']):
            ProductTagFactory(
                product=random.choice(products),
                tag=random.choice(tags),
            )
        
        for product in Product.objects.all():
            index_product(product)

        self.stdout.write(self.style.SUCCESS(
            f"✅ Seeded {options['products']} products, {options['tags']} tags, {options['taggings']} product-tag links"
        ))
