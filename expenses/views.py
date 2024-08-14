from django.shortcuts import render
from django.db.models import Sum, F
from .models import Expense, Payment
from django.utils import timezone

def expenses_dashboard(request):
    # Aggregate data
    total_outgoing_bills = Expense.objects.filter(is_outgoing=True).aggregate(total=Sum('amount'))['total'] or 0
    total_incoming_bills = Expense.objects.filter(is_outgoing=False).aggregate(total=Sum('amount'))['total'] or 0
    total_incoming_payment = Payment.objects.filter(is_outgoing=False).aggregate(total=Sum('amount'))['total'] or 0
    total_outgoing_payment = Payment.objects.filter(is_outgoing=True).aggregate(total=Sum('amount'))['total'] or 0

    # Example of calculating the percentage change from last month
    last_month = timezone.now().date().replace(day=1) - timezone.timedelta(days=1)
    current_month = timezone.now().date().replace(day=1)

    last_month_outgoing = Expense.objects.filter(is_outgoing=True, date__lt=current_month, date__gte=last_month).aggregate(total=Sum('amount'))['total'] or 0
    current_outgoing = Expense.objects.filter(is_outgoing=True, date__gte=current_month).aggregate(total=Sum('amount'))['total'] or 0

    outgoing_change = ((current_outgoing - last_month_outgoing) / last_month_outgoing * 100) if last_month_outgoing else 0

    # Data for the graph
    total_income_this_year = total_incoming_payment
    total_expense_this_year = total_outgoing_bills + total_outgoing_payment
    profit_this_year = total_income_this_year - total_expense_this_year

    context = {
        'total_outgoing_bills': total_outgoing_bills,
        'total_incoming_bills': total_incoming_bills,
        'total_incoming_payment': total_incoming_payment,
        'total_outgoing_payment': total_outgoing_payment,
        'outgoing_change': outgoing_change,
        'total_income_this_year': total_income_this_year,
        'total_expense_this_year': total_expense_this_year,
        'profit_this_year': profit_this_year,
    }

    return render(request, 'expenses/dashboard.html', context)
