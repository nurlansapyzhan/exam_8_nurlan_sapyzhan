from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import UpdateView, DeleteView

from reviewer.forms import ReviewForm
from reviewer.models import Product, Review


def create_review(request, pk):
    if request.user not in User.objects.all():
        raise ValidationError('You cant add review')
    else:
        product = get_object_or_404(Product, pk=pk)
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = Review()
                review.product = product
                review.author = request.user
                review.text = form.cleaned_data['text']
                review.rating = form.cleaned_data['rating']
                review.save()
                return redirect('product', pk=pk)
        else:
            form = ReviewForm()
        return render(request, 'add_review.html', {'form': form, 'product': product})


class ReviewUpdateView(UserPassesTestMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'update_review.html'
    context_object_name = 'review'

    def get_success_url(self):
        return reverse('index')

    def test_func(self):
        return self.request.user.has_perm('review.change_review') or self.request.user == self.model


class ReviewDeleteView(UserPassesTestMixin, DeleteView):
    model = Review
    template_name = 'delete_review.html'
    context_object_name = 'review'

    def get_success_url(self):
        return reverse('index')

    def test_func(self):
        return self.request.user.has_perm('review.change_review') or self.request.user == self.model
