from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from OpportuNest.accounts.forms import AccountTypeSelectionForm, CompanyCreationForm, SeekerCreationForm


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
                return redirect('register_company')
            elif account_type == 'seeker':
                return redirect('register_seeker')

        context = {
            'form': form,
        }

        return render(request, 'accounts/select_account_type.html', context)


class CompanyRegistrationView(CreateView):
    form_class = CompanyCreationForm
    template_name = 'accounts/register-company-profile.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        response = super().form_valid(form)

        login(self.request, self.object)

        return response


class SeekerRegistrationView(CreateView):
    form_class = SeekerCreationForm
    template_name = 'accounts/register-seeker-profile.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        response = super().form_valid(form)

        login(self.request, self.object)

        return response
