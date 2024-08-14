from django.db import models
from django.utils import timezone

class Expense(models.Model):
    date = models.DateField(default=timezone.now)
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_outgoing = models.BooleanField(default=True)  # True for outgoing, False for incoming

    def __str__(self):
        return f"{self.description} - {'Outgoing' if self.is_outgoing else 'Incoming'}: {self.amount}"

class Payment(models.Model):
    date = models.DateField(default=timezone.now)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
    is_outgoing = models.BooleanField(default=True)  # True for outgoing, False for incoming
    def __str__(self):
        return f"{'Outgoing' if self.is_outgoing else 'Incoming'} Payment: {self.amount}"
def percentage(current, previous):
    if previous == 0:
        return 0
    return (current - previous) / previous * 100






