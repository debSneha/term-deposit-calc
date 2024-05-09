from django import forms
from .models import TermDeposit

class TermDepositForm(forms.ModelForm):
    class Meta:
        model = TermDeposit
        fields = ['deposit_amount', 'interest_rate', 'term', 'interest_paid']