from django.db import models

class TermDeposit(models.Model):
    DEPOSIT_FREQUENCY_CHOICES = [
        ('monthly', 'Monthly'),
        ('quarterly', 'Quarterly'),
        ('annually', 'Annually'),
        ('at_maturity', 'At Maturity')
    ]

    deposit_amount = models.DecimalField(null=False, decimal_places=2, max_digits=20)
    interest_rate = models.DecimalField(null=False, decimal_places=2, max_digits=20)
    term = models.DecimalField(null=False, decimal_places=2, max_digits=20)
    interest_paid = models.CharField(null=False, max_length=50, choices=DEPOSIT_FREQUENCY_CHOICES)

    def calculate_final_balance(self):
        decimal_interest_rate = self.interest_rate / 100

        if self.interest_paid == 'monthly':
            final_balance = self.deposit_amount * (1 + decimal_interest_rate / 12) ** (12 * self.term)
        elif self.interest_paid == 'quarterly':
            final_balance = self.deposit_amount * (1 + decimal_interest_rate / 4) ** (4 * self.term)
        elif self.interest_paid == 'annually':
            final_balance = self.deposit_amount * (1 + decimal_interest_rate) ** self.term
        else:
            final_balance = self.deposit_amount * (1 + decimal_interest_rate * self.term)

        return round(final_balance, 2)


