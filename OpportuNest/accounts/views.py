from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from OpportuNest.accounts.forms import AccountTypeSelectionForm, CompanyCreationForm, SeekerCreationForm, \
    SeekerEditForm, CompanyEditForm
from OpportuNest.accounts.models import Company, Seeker
from OpportuNest.application.models import Application


class AccountSelectView(View):

    def get(self, request):
        form = AccountTypeSelectionForm()

        context = {
            'form': form,
        }

        return render(request, 'accounts/select_account_type.html', context)


    def post(self, request):
        form = AccountTypeSelectionForm(request.POST)

        if form.is_valid():
            account_type = form.cleaned_data['account_type']

            if account_type == 'company':
                return redirect('register-company')
            elif account_type == 'seeker':
                return redirect('register-seeker')

        context = {
            'form': form,
        }

        return render(request, 'accounts/select_account_type.html', context)


class CompanyRegistrationView(CreateView):
    form_class = CompanyCreationForm
    template_name = 'registration/register-company-profile.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        response = super().form_valid(form)

        login(self.request, self.object)

        return response


class SeekerRegistrationView(CreateView):
    form_class = SeekerCreationForm
    template_name = 'registration/register-seeker-profile.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        response = super().form_valid(form)

        login(self.request, self.object)

        return response


class ProfileDetailView(LoginRequiredMixin, DetailView):
    context_object_name = 'profile'

    def get_template_names(self):
        user = self.request.user

        if hasattr(user, 'company'):
            return 'accounts/company-profile-details.html'
        elif hasattr(user, 'seeker'):
            return 'accounts/seeker-profile-details.html'
        else:
            return 'common/index.html'


    def get_object(self, queryset=None):
        user = self.request.user

        if hasattr(user, 'company'):
            return user.company
        elif hasattr(user, 'seeker'):
            return user.seeker

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        if user.is_seeker:
            context['applications'] = user.applications.all()
        elif user.is_company:
            context['applications'] = Application.objects.filter(job__posted_by=user)

        return context

class EditSeekerView(LoginRequiredMixin, UpdateView):
    model = Seeker
    form_class = SeekerEditForm
    template_name = 'accounts/edit-seeker.html'

    def get_success_url(self):
        return reverse_lazy(
            'profile-details',
            kwargs={'pk': self.object.pk}
        )

    def get_object(self, queryset=None):
        user_id = self.kwargs.get('pk')
        return Seeker.objects.get(user_id=user_id)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class EditCompanyView(LoginRequiredMixin, UpdateView):
    model = Company
    form_class = CompanyEditForm
    template_name = 'accounts/edit-company.html'

    def get_success_url(self):
        return reverse_lazy(
            'profile-details',
            kwargs={'pk': self.object.pk}
        )

    def get_object(self, queryset=None):
        user_id = self.kwargs.get('pk')
        return Company.objects.get(user_id=user_id)


def delete_company_view(request, pk):
    company = get_object_or_404(Company, user_id=pk)

    if request.method == 'POST':
        user = company.user
        company.delete()
        user.delete()

        return redirect('index')

    context = {
        'company': company,
    }

    return render(request, 'registration/delete-account.html', context)

@login_required
def delete_seeker_view(request, pk):
    seeker = get_object_or_404(Seeker, user_id=pk)

    if request.method == "POST":
        user = seeker.user
        seeker.delete()
        user.delete()

        return redirect(reverse_lazy('index'))

    context = {
        'seeker': seeker,
    }

    return render(request, 'registration/delete-account.html', context)