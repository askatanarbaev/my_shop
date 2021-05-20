from django.urls import path
from .views import  ProductListView, CategoryListView, CategoryListView2

urlpatterns = [
    # path('', CategoryListView.as_view(), name='category'),
    path('', ProductListView.as_view(), name='product'),
    path('stoika/', CategoryListView.as_view(), name='catetory_detail'),
    path('formwork/', CategoryListView2.as_view(), name='catetory_detail2'),
    
]