from django.core.paginator import Paginator, \
    EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView, \
    ListView, DetailView
from django.shortcuts import get_object_or_404

from . import models
from cart.cart import Cart


class IndexView(TemplateView):
    template_name = 'shop/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = Cart(self.request)
        context['categories'] = models.Category.objects.all()
        context['latest_products'] = models.Product.objects.all()[:6]
        context['top_sellers'] = models.Product.objects.all()[:3]
        context['recently_viewed'] = models.Product.objects.all()[:3]
        context['top_new'] = models.Product.objects.all()[:3]
        return context


class ProductListView(ListView):
    template_name = 'shop/product/list.html'
    model = models.Product
    paginate_by = 8

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = Cart(self.request)
        context['categories'] = models.Category.objects.all()

        product_list = models.Product.objects.filter(available=True)

        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            category = get_object_or_404(models.Category, slug=category_slug)
            context['object_list'] = product_list.filter(category=category)

        paginator = Paginator(product_list, self.paginate_by)
        page_number = self.request.GET.get('page', 1)
        try:
            products = paginator.page(page_number)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)

        context['object_list'] = products
        return context


class ProductDetailView(DetailView):
    template_name = 'shop/product/detail.html'
    model = models.Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = Cart(self.request)
        context['categories'] = models.Category.objects.all()
        context['other_products'] = models.Product.objects.exclude(id=self.object.id)[:4]
        return context
