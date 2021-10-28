from django.shortcuts import render
from django.views.generic import ListView, DetailView

from products.models import ProductModel, CategoryModel, BrandModel, ProductTagModel


class ProductsListView(ListView):
    template_name = 'products.html'
    paginate_by = 3

    def get_queryset(self):
        qs = ProductModel.objects.order_by('-pk')

        q = self.request.GET.get('q')
        cat = self.request.GET.get('cat')
        brand = self.request.GET.get('brand')
        tag = self.request.GET.get('tag')
        sort = self.request.GET.get('sort')
        size = self.request.GET.get('size')
        price = self.request.GET.get('price')
        color = self.request.GET.get('color')

        if q:
            qs = qs.filter(title__icontains=q)

        if cat:
            qs = qs.filter(category_id=cat)

        if brand:
            qs = qs.filter(brand_id=brand)

        if tag:
            qs = qs.filter(tags__id=tag)

        if color:
            qs = qs.filter(colors__id=color)

        if size:
            qs = qs.filter(sizes__id=size)

        if price:
            price_from, price_to = price.split(';')
            qs = qs.filter(real_price__gte=price_from, real_price__lte=price_to)

        if sort:
            if sort == 'price':
                qs = qs.order_by('real_price')
            elif sort == '-price':
                qs = qs.order_by('-real_price')
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CategoryModel.objects.order_by('-pk')
        context['brands'] = BrandModel.objects.order_by('-pk')
        context['tags'] = ProductTagModel.objects.order_by('-pk')
        context['size'] = ProductTagModel.objects.order_by('-pk')
        return context


class ProductDetailView(DetailView):
    template_name = 'product.html'
    model = ProductModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related'] = self.object.category.products.exclude(pk=self.object.pk)[:4]
        return context
