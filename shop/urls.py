from django.urls import path
from .views import  ProductListView, CategoryListView, CategoryListView2, ProductDetailView

urlpatterns = [
    # path('', CategoryListView.as_view(), name='category'),
    path('', ProductListView.as_view(), name='home'),
    path('stoika/', CategoryListView.as_view(), name='catetory_detail'),
    path('formwork/', CategoryListView2.as_view(), name='catetory_detail2'),
    path('product/<str:slug>/', ProductDetailView.as_view(), name='product_detail'),
    # path('modal-product/<int:pk>/', modalproduct, name='modal-product'),

]