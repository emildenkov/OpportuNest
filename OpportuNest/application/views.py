import os

import cloudinary
import cloudinary.uploader
import cloudinary.api
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.http import Http404

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
def view_resume(request, pk):
    application = get_object_or_404(Application, pk=pk)

    if not (request.user.is_staff or request.user == application.job.posted_by):
        raise PermissionDenied("You are not allowed to view this resume")

    resume_resource = application.resume

    public_id = resume_resource.public_id
    file_format = resume_resource.format
    resource_type = 'raw'

    try:
        resume_url, _ = cloudinary.utils.cloudinary_url(
            public_id,
            resource_type=resource_type,
            format=file_format,
            secure=True,
            sign_url=True
        )

        print(f"Generated URL: {resume_url}")

        return redirect(resume_url)

    except Exception as e:
        print(f"Error generating resume URL: {e}")
        raise Http404('Resume not found')