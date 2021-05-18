from django.urls import path
from .views import CategoryListView

urlpatterns = [
    # path('', post_list, name='home'),
    path('', CategoryListView.as_view(), name='category'),
]