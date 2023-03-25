from django.urls import path

from reviewer.views.products import ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product'),
    path('product/add', ProductCreateView.as_view(), name='add_product'),
    path('product/<int:pk>/edit', ProductUpdateView.as_view(), name='product_edit'),
    path('product/<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),
    path('product/<int:pk>/confirm_delete', ProductDeleteView.as_view(), name='confirm_delete'),
]
