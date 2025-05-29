from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=30)  # e.g., "fashion"
    class Meta:
        db_table = "app_tags"

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    image = models.ImageField(upload_to="products/", null=True, blank=True)
    tag_vector = models.JSONField(null=True, blank=True)

    tags = models.ManyToManyField(Tag, related_name="products", through="ProductTag")
    class Meta:
        db_table = "app_products" 


class ProductTag(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_tags')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name="tag_links")
    confidence = models.FloatField()
    source = models.CharField(max_length=20)  # e.g., "clip", "manual"
    class Meta:
        db_table = "app_products_tags"