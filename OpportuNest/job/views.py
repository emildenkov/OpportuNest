from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, FormView
from rest_framework.generics import ListAPIView

from OpportuNest.job.forms import AddJobForm, EditJobForm, DeleteJobForm, SearchJobForm
from OpportuNest.job.models import Job
from OpportuNest.job.serializers import JobSerializer


class JobListView(LoginRequiredMixin, ListView, FormView):
    model = Job
    template_name = 'job/job-list.html'
    context_object_name = 'job_list'
    paginate_by = 5
    form_class = SearchJobForm

    def get_queryset(self):
        queryset = self.model.objects.select_related('posted_by__company')

        query = self.request.GET.get('query', None)

        if query:
            queryset = queryset.filter(title__icontains=query)

        return queryset


class AddJobView(LoginRequiredMixin, CreateView):
    model = Job
    template_name = 'job/add-job.html'
    form_class = AddJobForm
    success_url = reverse_lazy('job-list')

    def form_valid(self, form):
        job = form.save(commit=False)

        job.posted_by = self.request.user

        return super().form_valid(form)


class DetailJobView(LoginRequiredMixin, DetailView):
    model = Job
    template_name = 'job/details-job.html'

    def get_queryset(self):
        return Job.objects.select_related('posted_by__company')


class EditJobView(LoginRequiredMixin, UserPassesTestMixin,  UpdateView):
    model = Job
    form_class = EditJobForm
    template_name = 'job/edit-job.html'

    def test_func(self):
        job = get_object_or_404(Job, pk=self.kwargs['pk'])

        return self.request.user == job.posted_by

    def get_success_url(self):
        return reverse_lazy(
            'job-details',
            kwargs={
                'pk': self.kwargs['pk']
            }
)


class DeleteJobView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Job
    success_url = reverse_lazy('job-list')
    template_name = 'job/delete-job.html'
    form_class = DeleteJobForm

    def test_func(self):
        job = get_object_or_404(Job, pk=self.kwargs['pk'])
        return self.request.user == job.posted_by

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)


class JobListAPIView(ListAPIView):
    queryset = Job.objects.all().order_by('-date_posted')
    serializer_class = JobSerializer