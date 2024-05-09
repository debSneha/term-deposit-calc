
# Create your views here.
from django.shortcuts import render
from django.views.generic import FormView
from .forms import TermDepositForm
from .models import TermDeposit

class TermDepositCalculator(FormView):
    template_name = "tdCalculator.html"
    form_class = TermDepositForm
    success_url = '/calculator'

    def form_valid(self, form):
        term_deposit = form.save(commit=False)
        final_balance = float(term_deposit.calculate_final_balance())
        self.request.session['final_balance'] = final_balance
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        final_balance = self.request.session.pop('final_balance', None)
        context['final_balance'] = final_balance
        return context
