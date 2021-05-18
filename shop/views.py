from django.shortcuts import render
from .models import Category
from django.views.generic.list import ListView
from django.utils import timezone

def post_list(request):
    all_models = Category.objects.all()
    return render(request, "home.html", locals())


class CategoryListView(ListView):
    model = Category
    template_name = 'home.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        return context 


    