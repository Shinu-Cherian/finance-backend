from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum
from finance.models import FinancialRecord

@api_view(['GET'])
def dashboard_summary(request):
    total_income = FinancialRecord.objects.filter(type='income').aggregate(Sum('amount'))['amount__sum'] or 0
    total_expense = FinancialRecord.objects.filter(type='expense').aggregate(Sum('amount'))['amount__sum'] or 0

    balance = total_income - total_expense

    return Response({
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": balance
    })