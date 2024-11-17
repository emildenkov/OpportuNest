from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from OpportuNest.job.forms import AddJobForm
from OpportuNest.job.models import Job


class JobListView(LoginRequiredMixin, ListView):
    model = Job
    template_name = 'job/job-list.html'
    context_object_name = 'job_list'
    paginate_by = 5

    def get_queryset(self):
        return Job.objects.select_related('posted_by__company')

class AddJobView(LoginRequiredMixin, CreateView):
    model = Job
    template_name = 'job/add-job.html'
    form_class = AddJobForm
    success_url = reverse_lazy('job-list')

    def form_valid(self, form):
        job = form.save(commit=False)
        job.posted_by = self.request.user

        return super().form_valid(form)
