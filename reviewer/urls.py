from django.urls import path

from reviewer.views.products import ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, IndexView
from reviewer.views.reviews import create_review, ReviewUpdateView, ReviewDeleteView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product'),
    path('product/add', ProductCreateView.as_view(), name='add_product'),
    path('product/<int:pk>/edit', ProductUpdateView.as_view(), name='product_edit'),
    path('product/<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),
    path('product/<int:pk>/confirm_delete', ProductDeleteView.as_view(), name='confirm_delete'),
    path('product/<int:pk>/add_review', create_review, name='add_review'),
    path('product/<int:pk>/update_review/', ReviewUpdateView.as_view(), name='update_review'),
    path('product/<int:pk>/delete_review/', ReviewDeleteView.as_view(), name='delete_review'),
]
