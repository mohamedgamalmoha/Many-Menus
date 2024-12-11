from django.shortcuts import get_object_or_404

from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.settings import api_settings
from rest_framework.viewsets import ReadOnlyModelViewSet

from drf_spectacular.utils import extend_schema
from rest_flex_fields.utils import is_expanded
from rest_flex_fields.views import FlexFieldsMixin
from rest_flex_fields.filter_backends import FlexFieldsFilterBackend

from ..models import Restaurant, Category, Product
from .filters import RestaurantFilterSet, CategoryFilterSet, ProductFilterSet
from .serializer import RestaurantSerializer, CategorySerializer, ProductSerializer


class RestaurantViewSet(FlexFieldsMixin, ReadOnlyModelViewSet):
    queryset = Restaurant.objects.filter(is_active=True)
    serializer_class = RestaurantSerializer
    permission_classes = [AllowAny]
    filter_backends = [FlexFieldsFilterBackend] + api_settings.DEFAULT_FILTER_BACKENDS
    permit_list_expands = ['owner', 'header_images', 'social_media_links']
    filterset_class = RestaurantFilterSet
    lookup_field = 'slug'

    def get_queryset(self):
        queryset = super().get_queryset()
        if is_expanded(self.request, 'owner'):
            queryset = queryset.select_related('owner')
        if is_expanded(self.request, 'header_images'):
            queryset = queryset.select_related('header_images')
        if is_expanded(self.request, 'social_media_links'):
            queryset = queryset.select_related('social_media_links')
        if self.action == 'categories':
            queryset = queryset.select_related('categories')
        return queryset

    @extend_schema(responses={200: CategorySerializer(many=True)}, filters=True)
    @action(["GET"], detail=True, url_path='categories', queryset=Category.objects.none(),
            serializer_class=CategorySerializer, filterset_class=CategoryFilterSet, lookup_field='slug')
    def categories(self, request, *args, **kwargs):
        # Create a dictionary of filter arguments using the lookup field (e.g., 'id') and its value from the URL kwargs
        filter_kwargs = {self.lookup_field: self.kwargs[self.lookup_field]}

        # Retrieve the specific Restaurant object that matches the filter arguments.
        # If no Restaurant is found, raise a 404 error.
        restaurant = get_object_or_404(Restaurant, **filter_kwargs)

        # Dynamically set the filterset class to be used for filtering categories in the current request.
        self.filterset_class = CategoryFilterSet

        # Dynamically set the serializer class to CategorySerializer for serializing the response.
        self.serializer_class = CategorySerializer

        # Set the queryset to be the categories associated with the retrieved restaurant.
        self.queryset = restaurant.categories.all()

        # Delegate to the `list` method to handle filtering, pagination, and serialization of the queryset.
        return self.list(request, *args, **kwargs)


class CategoryViewSet(FlexFieldsMixin, ReadOnlyModelViewSet):
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]
    filter_backends = [FlexFieldsFilterBackend] + api_settings.DEFAULT_FILTER_BACKENDS
    permit_list_expands = ['variants']
    filterset_class = CategoryFilterSet

    def get_queryset(self):
        queryset = super().get_queryset()
        if is_expanded(self.request, 'products') or self.action == 'products':
            queryset = queryset.select_related('products')
        return queryset

    @extend_schema(responses={200: ProductSerializer}, filters=True)
    @action(["GET"], detail=True, url_path='products', queryset=Product.objects.none(),
            serializer_class=ProductSerializer, filterset_class=ProductFilterSet)
    def products(self, request, *args, **kwargs):
        # Create a dictionary of filter arguments using the lookup field (e.g., 'id') and its value from the URL kwargs
        filter_kwargs = {self.lookup_field: self.kwargs[self.lookup_field]}

        # Retrieve the specific Category object that matches the filter arguments.
        # If no Category is found, raise a 404 error.
        category = get_object_or_404(Category, **filter_kwargs)

        # Dynamically set the filterset class to be used for filtering products in the current request.
        self.filterset_class = ProductFilterSet

        # Dynamically set the serializer class to ProductSerializer for serializing the response.
        self.serializer_class = ProductSerializer

        # Set the queryset to be the products associated with the retrieved category.
        self.queryset = category.products.all()

        # Delegate to the `list` method to handle filtering, pagination, and serialization of the queryset.
        return self.list(request, *args, **kwargs)
