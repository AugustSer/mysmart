from django.urls import path

from . import views

app_name = 'shop'

urlpatterns = [
    path('products/',
         views.ProductListView.as_view(),
         name='product_list'),
    path('products/<slug:category_slug>/',
         views.ProductListView.as_view(),
         name='product_list_by_category'),
    path('products/<int:pk>/<slug:slug>/',
         views.ProductDetailView.as_view(),
         name='product_detail'),
    path('',
         views.IndexView.as_view(),
         name='home')
]
