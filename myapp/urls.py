from django.urls import path
from .views import upload_product_image

urlpatterns = [
    path('upload-product-image/', upload_product_image, name='upload-product-image'),
    path('upload-product-image/', upload_product_image, name='upload-product-image'),
]

