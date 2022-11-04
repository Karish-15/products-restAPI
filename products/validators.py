from rest_framework import validators
from .models import Product

unique_title_validator = validators.UniqueValidator(queryset=Product.objects.all())