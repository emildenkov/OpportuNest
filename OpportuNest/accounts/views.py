from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView
from OpportuNest.accounts.forms import AccountTypeSelectionForm, CompanyCreationForm, SeekerCreationForm, \
    SeekerEditForm, CompanyEditForm
from OpportuNest.accounts.models import Company, Seeker


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