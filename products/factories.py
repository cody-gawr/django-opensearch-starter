import os
import factory
import random
from django.core.files import File
from faker import Faker
from products.models import Product, Tag, ProductTag

fake = Faker()

SEED_IMAGE_DIR = "media/seed_images/products"

class TagFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tag

    name = factory.LazyAttribute(lambda _: fake.word())
    category = factory.LazyAttribute(lambda _: random.choice(["fashion", "electronics"]))

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.LazyAttribute(lambda _: fake.word().capitalize() + " " + fake.color_name())
    description = factory.Faker('sentence')
    price = factory.LazyAttribute(lambda _: round(random.uniform(10, 200), 2))

    @factory.lazy_attribute
    def image(self):
        images = os.listdir(SEED_IMAGE_DIR)
        image_name = random.choice(images)
        image_path = os.path.join(SEED_IMAGE_DIR, image_name)
        return File(open(image_path, "rb"), name=image_name)

class ProductTagFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductTag

    product = factory.SubFactory(ProductFactory)
    tag = factory.SubFactory(TagFactory)
    confidence = factory.LazyAttribute(lambda _: round(random.uniform(0.5, 1.0), 2))
    source = "seed"