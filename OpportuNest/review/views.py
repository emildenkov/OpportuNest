from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from OpportuNest.review.forms import CreateReviewForm
from OpportuNest.review.models import Review


class CreateReviewView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = CreateReviewForm
    template_name = 'reviews/create-review.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        review = form.save(commit=False)
        review.reviewer = self.request.user

        return super().form_valid(form)
