from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

from .models import Product

@register(Product)
class ProductIndex(AlgoliaIndex):
    # should_index='is_public'
    fields = [
        'title',
        'body',
        'user',
        'price', 
        'public'
    ]

    settings = {
        'searchableAttributes': ['title', 'body'],
        'attributesForFaceting': ['users', 'public']
    }