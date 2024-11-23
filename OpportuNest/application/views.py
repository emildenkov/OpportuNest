import requests
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from OpportuNest.application.forms import CreateApplicationForm
from OpportuNest.application.models import Application
from OpportuNest.job.models import Job


class CreateApplicationView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Application
    form_class = CreateApplicationForm
    template_name = 'applications/create-application.html'
    success_url = reverse_lazy('job-list')

    def form_valid(self, form):
        application = form.save(commit=False)

        application.applicant = self.request.user
        application.job = get_object_or_404(Job, pk=self.kwargs['job_id'])

        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_seeker


class DetailApplicationView(LoginRequiredMixin, DetailView):
    model = Application
    template_name = 'applications/details-application.html'
    context_object_name = 'application'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        application = self.get_object()

        context['company_name'] = application.job.posted_by.company.company_name
        context['applicant_email'] = application.applicant.email

        return context

@login_required
@user_passes_test(lambda user: user.is_company)
def accept_application(request, pk):
    application = get_object_or_404(Application, pk=pk)
    if application.job.posted_by == request.user:
        application.status = 'Accepted'
        application.save()
        return redirect('profile-details', pk=request.user.pk)


@login_required
@user_passes_test(lambda user: user.is_company)
def reject_application(request, pk):
    application = get_object_or_404(Application, pk=pk)
    if application.job.posted_by == request.user:
        application.status = 'Rejected'
        application.save()
        return redirect('profile-details', pk=request.user.pk)


@login_required
def download_resume(request, pk):      #TODO: fix this view!!!
    try:
        application = get_object_or_404(Application, pk=pk)

        if not(request.user.is_staff or request.user == application.job.posted_by):
            raise PermissionDenied("You are not allowed to download this resume")

        resume_url = application.resume.url
        response = requests.get(resume_url)

        if response.status_code != 200:
            raise Http404('Resume not found')

        filename = resume_url.split('/')[-1].split('?')[0]

        response_content = HttpResponse(
            response.content,
            content_type='application/pdf',
        )

        response_content['Content-Disposition'] = f'attachment; filename="{filename}"'
        return response_content

    except Application.DoesNotExist:
        raise Http404('Application not found')
