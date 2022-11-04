from rest_framework import serializers
from rest_framework.reverse import reverse

from api.serializers import UserPublicSerializer
from .models import Product
from . import validators


class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source = 'user', read_only=True)
    url = serializers.SerializerMethodField(read_only = True)
    title = serializers.CharField(validators = [validators.unique_title_validator])
    body = serializers.CharField(source = 'content')
    '''
    ALTERNATIVE, WITHOUT DEFINING A METHOD
    url = serializers.HyperLinkedIdentityField(
        view_name = 'product-detail', 
        lookup_field = 'pk'
    )
    '''
    class Meta:
        model = Product
        fields = [
            'owner',
            'url',
            'pk',
            'title',
            # 'content',
            'body',
            'price',
            'sale_price',
        ]
    # def validate_title(self, value):
    #     qs = Product.objects.filter(title__exact = value)
    #     if qs.exists() and self.context.get('request').method == 'POST':
    #         raise serializers.ValidationError(f"{value} exists in database")
    #     return value
    def validate_content(self, value):
        if not value:
            return self.initial_data['title']
        return value
    
    def get_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-detail", kwargs = {"pk": obj.pk}, request = request)