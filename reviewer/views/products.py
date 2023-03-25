from django.contrib.auth.mixins import UserPassesTestMixin
from django.db.models import Q
from django.urls import reverse, reverse_lazy
from django.utils.http import urlencode
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

from reviewer.forms import ProductForm, SearchForm
from reviewer.models import Product, Review


class IndexView(ListView):
    template_name = 'index.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 6
    paginate_orphans = 0

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(name__icontains=self.search_value) | Q(description__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None


class ProductDetailView(DetailView):
    template_name = 'product_detail.html'
    model = Product

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        reviews = Review.objects.all().filter(product=self.object.pk)
        total_rating = 0
        for review in reviews:
            total_rating += review.rating
        review_counter = len(reviews)
        if review_counter == 0:
            avarage = 0
        else:
            avarage = total_rating / review_counter
        kwargs['reviews'] = reviews
        kwargs['avarage'] = avarage
        return super().get_context_data(**kwargs)


class ProductCreateView(UserPassesTestMixin, CreateView):
    template_name = 'add_product.html'
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('product', kwargs={'pk': self.object.pk})

    def test_func(self):
        return self.request.user.has_perm('product.add_product')


class ProductUpdateView(UserPassesTestMixin, UpdateView):
    template_name = 'product_edit.html'
    form_class = ProductForm
    model = Product

    def get_success_url(self):
        return reverse('product', kwargs={'pk': self.object.pk})

    def test_func(self):
        return self.request.user.has_perm('product.change_product')


class ProductDeleteView(UserPassesTestMixin, DeleteView):
    template_name = 'product_delete_confirm.html'
    model = Product
    context_object_name = 'product'
    success_url = reverse_lazy('index')

    def test_func(self):
        return self.request.user.has_perm('product.delete_product')
