from django.core.management.base import BaseCommand
from search.opensearch_client import client

class Command(BaseCommand):
    help = "Create the OpenSearch index for products"

    def handle(self, *args, **kwargs):
        mapping = {
            "mappings": {
                "properties": {
                    "id": {"type": "integer"},
                    "name": {"type": "text"},
                    "description": {"type": "text"},
                    "tags": {"type": "keyword"},
                    "tag_vector": {
                        "type": "dense_vector",
                        "dims": 512,  # for CLIP ViT-B/32
                        "index": True,
                        "similarity": "cosine"
                    }
                }
            }
        }

        if client.indices.exists(index="products"):
            client.indices.delete(index="products")

        client.indices.create(index="products", body=mapping)
        self.stdout.write(self.style.SUCCESS("✅ Created OpenSearch index 'products'"))
