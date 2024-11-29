from django.db.models import Avg
from django.shortcuts import render
from django.views.generic import TemplateView

from OpportuNest.review.models import Review


class IndexView(TemplateView):
    template_name = 'common/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['average_rating'] = Review.objects.aggregate(avg_rating=Avg('rating'))['avg_rating']

        return context
