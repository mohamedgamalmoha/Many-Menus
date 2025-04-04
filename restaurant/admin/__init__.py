from django.contrib import admin

from ..sites import customer_admin_site
from ..models import Restaurant, Category, Product, ProductVariant, ProductType
from .customer import (RestaurantCustomerAdmin, CategoryCustomerAdmin, ProductCustomerAdmin,
                       ProductVariantsCustomerAdmin)
from .superuser import (RestaurantSuperuserAdmin, CategorySuperuserAdmin, ProductSuperuserAdmin,
                        ProductVariantSuperuserAdmin, ProductTypeSuperuserAdmin)


customer_admin_site.register(Restaurant, RestaurantCustomerAdmin)
customer_admin_site.register(Category, CategoryCustomerAdmin)
customer_admin_site.register(ProductVariant, ProductVariantsCustomerAdmin)
customer_admin_site.register(Product, ProductCustomerAdmin)

admin.site.register(Restaurant, RestaurantSuperuserAdmin)
admin.site.register(Category, CategorySuperuserAdmin)
admin.site.register(ProductVariant, ProductVariantSuperuserAdmin)
admin.site.register(ProductType, ProductTypeSuperuserAdmin)
admin.site.register(Product, ProductSuperuserAdmin)
